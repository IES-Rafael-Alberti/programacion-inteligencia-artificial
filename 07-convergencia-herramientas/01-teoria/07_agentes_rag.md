# F6 — Agentes y RAG en Producción

**RA/CE**: RA3e (toma de decisiones basada en datos)
**Duración**: 4h teoría + 6h práctica
**Prerrequisitos**: UD6 (LangChain, RAG básico, Ollama), F5 (serving APIs), F3 (Model Registry)

---

## Recordatorio: RAG tradicional (de Modelos de la IA)

En la unidad **Modelos de la IA** (UD6) trabajaste el RAG tradicional: fragmentar documentos en chunks de tamaño fijo, generar embeddings con modelos como `all-MiniLM-L6-v2`, almacenarlos en un vector store (ChromaDB) y recuperar los top-k chunks más similares a la consulta mediante búsqueda por similitud coseno. Ese enfoque es efectivo para knowledge bases planas donde todos los documentos están al mismo nivel (p.ej., documentación técnica, FAQs). En esta unidad asumimos que conoces esos fundamentos — si necesitas repasarlos, consulta la práctica `101_rag_chromadb_ollama.ipynb` de UD6.

Sin embargo, el RAG plano tiene limitaciones importantes cuando los documentos tienen **estructura jerárquica** (empresa → departamento → proyecto → tarea) o cuando las consultas requieren información de varios niveles simultáneamente. Para esos casos necesitamos **indexación jerárquica**.

---

## 1. Indexación Jerárquica

### 1.1 Limitaciones del RAG plano

El RAG plano con ChromaDB + top-k chunks funciona bien cuando:

- Los documentos son independientes y del mismo tipo
- La consulta se responde con uno o dos fragmentos
- No hay relaciones padre-hijo entre documentos

Pero falla cuando:

- **Contexto perdido**: un chunk sobre "tarifa nocturna" no contiene la información de qué parking la aplica ni a qué cliente pertenece
- **Granularidad incorrecta**: chunks de 512 tokens pueden ser demasiado pequeños para conceptos globales (políticas de empresa) y demasiado grandes para detalles específicos (precio por hora de un parking concreto)
- **Ruido en recuperación**: chunks de distintos niveles compiten en el ranking de similitud, mezclando información de empresa con detalles de vehículo sin relación

### 1.2 Qué es indexación jerárquica

La indexación jerárquica organiza los documentos en un **árbol de nodos** donde:

- **Nodos raíz**: resúmenes o políticas globales (nivel empresa)
- **Nodos intermedios**: categorías o agrupaciones (nivel parking, nivel cliente)
- **Nodos hoja**: detalles específicos (nivel vehículo, nivel transacción)

Cada nodo contiene su propio texto, metadatos que describen su posición en la jerarquía y referencias a nodos padre e hijo:

```
                  Empresa ParkingCorp
                 /         |         \
        Parking Norte  Parking Sur  Parking Centro
           /     \          |            /    \
      Cliente A  Cliente B  Cliente C  ...   ...
        |           |           |
    Vehículo X   Vehículo Y  Vehículo Z
```

Cuando un usuario pregunta "¿cuánto paga el cliente A por hora en Parking Norte?", el recuperador navega: Empresa → Parking Norte → Cliente A → Tarifas, y responde con el nodo hoja correcto usando el contexto de los nodos ancestros.

### 1.3 LlamaIndex: HierarchicalNodeParser + RecursiveRetriever

**LlamaIndex** proporciona `HierarchicalNodeParser` para construir el árbol documental y `RecursiveRetriever` para navegarlo:

```python
from llama_index.core import Document
from llama_index.core.node_parser import HierarchicalNodeParser
from llama_index.core.retrievers import RecursiveRetriever
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

# Configurar embeddings locales (HuggingFace)
Settings.embed_model = HuggingFaceEmbedding(
    model_name="all-MiniLM-L6-v2"
)

# Documento con estructura jerárquica
doc_text = """
# ParkingCorp — Políticas Corporativas

## Misión
ParkingCorp gestiona 23 aparcamientos en la ciudad.

## Tarifas generales
Tarifa base: 2 €/hora en parking estándar, 3 €/hora en premium.

## Horarios
Todos los parkings abren de 7:00 a 23:00.

---

## Parking Norte
Dirección: Calle Mayor 15 · Capacidad: 200 plazas
Tarifa: 2,50 €/hora (recargo céntrico)
Abonos mensuales: Básico 80 €, Premium 120 €

## Parking Sur
Dirección: Avda. del Puerto 42 · Capacidad: 350 plazas
Tarifa: 1,80 €/hora · Tarifa plana nocturna: 5 €

---

## Cliente A — Abono Premium Plus
Plan: 120 €/mes | Vehículos permitidos: 2
Forma de pago: domiciliación bancaria

## Vehículo X — 1234ABC
Tipo: Turismo | Abono: Premium Plus
Último acceso: 15/06/2026 08:30
Última incidencia: Disputa de multa — 10/06/2026
"""

document = Document(text=doc_text)

# Jerarquía: chunk grande = empresa, mediano = parking, pequeño = detalle
parser = HierarchicalNodeParser.from_defaults(
    chunk_sizes=[2048, 512, 128]
)
nodes = parser.get_nodes_from_documents([document])

# Recuperador recursivo: navega padre → hijo según la consulta
retriever = RecursiveRetriever(
    vector_retriever=index.as_retriever(similarity_top_k=3),
    node_parser=parser,
    verbose=True
)

# Consulta que cruza niveles
respuesta = retriever.retrieve(
    "¿Cuánto paga el Cliente A por hora en Parking Norte?"
)
```

El flujo interno de `RecursiveRetriever`:

1. **Busca nodos hoja** relevantes a la consulta (nivel detalle)
2. **Asciende al padre** si el contexto del nodo hoja es insuficiente
3. **Desciende a hijos** del nodo padre si la consulta requiere granularidad fina
4. **Repite** hasta reunir contexto suficiente de todos los niveles implicados

### 1.4 Patrones de indexación para documentos empresariales

| Patrón | Descripción | Caso parking |
|--------|-------------|-------------|
| **Top-down jerárquico** | Empresa → División → Departamento → Documento | ParkingCorp → Parking → Cliente → Vehículo |
| **Por tipo de documento** | Políticas / Contratos / Informes en ramas separadas | Tarifas en rama política, incidencias en rama operativa |
| **Híbrido con metadatos** | Árbol + filtros por etiquetas (fecha, categoría, prioridad) | Transacciones con metadatos de fecha y tipo de pago |
| **Ventana deslizante con solapamiento** | Chunks que comparten contexto con el nodo anterior | Contratos largos con cláusulas que cruzan chunks |

> **Nota sobre la indexación jerárquica**: Elige indexación jerárquica cuando tus documentos tengan relaciones explícitas padre-hijo, las consultas necesiten contexto multinivel o los chunks planos pierdan información de estructura. Para knowledge bases planas sin jerarquía, el RAG tradicional con ChromaDB sigue siendo más simple y eficiente. No sobreingenierices la jerarquía donde no hace falta.

### Guía práctica de tuning de `chunk_sizes`

El parámetro `chunk_sizes` define el tamaño (en tokens) de cada nivel jerárquico. Cada nivel resume al anterior, de mayor a menor granularidad:

```python
# Estructura típica: [nivel_padre, nivel_hijo, nivel_detalle]
chunk_sizes=[2048, 512, 128]  # empresa → parking → transacción
```

| Niveles | Cuándo usarlo | Ejemplo |
|---------|---------------|---------|
| `[4096]` | Documentos planos sin jerarquía (no necesitas indexación jerárquica, usa RAG tradicional) | FAQs, documentación técnica plana |
| `[2048, 512]` | Documentos con 2 niveles (sección + detalle) | Informes, artículos, guías |
| `[2048, 512, 128]` | Documentos con 3 niveles (dominio + categoría + detalle) | **ParkingCorp**, documentación empresarial |
| `[4096, 1024, 256]` | Documentos muy extensos (>50 páginas) donde el nivel padre debe capturar contexto completo | Manuales técnicos, contratos largos |
| `[1024, 256, 64]` | Documentos cortos donde se necesita granularidad muy fina (ej. tuits, reseñas) | Análisis de feedback, logs |

**Reglas prácticas**:
1. El nivel padre debe ser **2-4× el nivel hijo** — si la diferencia es menor, la jerarquía aporta poco
2. El nivel más pequeño (hoja) debe tener el tamaño mínimo necesario para responder consultas atómicas — 128 tokens es un buen punto de partida
3. Más de 4 niveles empeora el rendimiento — la recuperación se vuelve lenta y el ruido aumenta
4. Prueba con 3 consultas representativas de tu dominio ajustando `chunk_sizes` hasta que las respuestas tengan el contexto completo sin exceso
5. Si no estás seguro: empieza con `[2048, 512, 128]` (el más usado en producción) y ajusta según resultados

---

## 2. Sistemas Multi-Agente sobre Índices Jerárquicos

### 2.1 Por qué combinar multi-agente con indexación jerárquica

Un sistema multi-agente sobre índices jerárquicos resuelve tres problemas que ni los agentes solos ni la indexación plana resuelven por separado:

1. **Routing inteligente**: el agente clasificador determina qué nivel del árbol consultar según la intención de la consulta
2. **Recuperación contextual**: el agente recuperador navega el árbol con conciencia del nivel actual, no en frío
3. **Validación multinivel**: el agente validador comprueba que la respuesta es coherente en todos los niveles de la jerarquía

**Conexión RA3e**: La toma de decisiones basada en datos (RA3e) se materializa cuando múltiples agentes navegan la jerarquía documental con conciencia del contexto completo de cada nivel. Un agente que consulta tarifas de parking sabe no solo el precio, sino también qué cliente aplica, qué política corporativa lo rige y qué vehículo está involucrado.

### 2.2 Caso parking: estructura documental jerárquica

Tomemos **ParkingCorp**, empresa de gestión de aparcamientos, como caso de estudio. Su documentación tiene una jerarquía natural:

```
Nivel 1: Empresa (ParkingCorp)
├── Políticas corporativas (tarifas generales, horarios, condiciones)
├── Plantilla de contratos
└── Informes financieros globales

Nivel 2: Parking (individual)
├── Parking Norte (dirección, capacidad, tarifas específicas)
├── Parking Sur (dirección, horario ampliado, tarifa plana nocturna)
└── Parking Centro (parking premium, servicio de lavado)

Nivel 3: Cliente
├── Cliente A (abono mensual Premium, 2 vehículos)
├── Cliente B (abono trimestral Básico, 1 vehículo)
└── Cliente C (pago por uso, sin abono)

Nivel 4: Vehículo
├── 1234ABC (turismo, asociado a Cliente A)
├── 5678DEF (motocicleta, asociado a Cliente A)
└── 9012GHI (furgoneta, tarifa especial)

Nivel 5: Transacción / Incidencia
├── Pago Parking Norte 15/06 (5 € — 2h)
├── Disputa multa 1234ABC (apelación recibida)
└── Pérdida de ticket Cliente B (recargo 20 €)
```

Este caso es ideal para indexación jerárquica porque una consulta como "¿puede el cliente A entrar al Parking Centro con su abono?" requiere información de tres niveles: Empresa (políticas de uso de abonos), Parking Centro (reglas específicas), Cliente A (abono contratado). Un RAG plano devolvería chunks inconexos; la indexación jerárquica los relaciona.

### 2.3 Implementación con CrewAI + LlamaIndex

El sistema multi-agente combina CrewAI para la orquestación y LlamaIndex para la recuperación jerárquica:

```python
from crewai import Agent, Task, Crew, Process
from llama_index.core.retrievers import RecursiveRetriever

# Herramienta: recuperación jerárquica
class HierarchicalRetrieverTool(BaseTool):
    name: str = "Recuperador Jerárquico"
    description: str = (
        "Busca información en la base documental jerárquica del parking. "
        "Usa índices por niveles: empresa, parking, cliente, vehículo, transacción."
    )

    def _run(self, query: str, nivel: str = "auto") -> str:
        nodes = recursive_retriever.retrieve(query)
        results = [
            n for n in nodes
            if nivel == "auto" or n.metadata.get("nivel") == nivel
        ]
        return formatear_resultados(results)

# Agente 1: Clasificador de consultas
clasificador = Agent(
    role="Clasificador de Consultas del Parking",
    goal="Determinar qué nivel de la jerarquía del parking necesita la consulta",
    backstory="Experto en el dominio de gestión de aparcamientos. "
              "Sabe si una pregunta es sobre políticas corporativas, "
              "un parking concreto, un cliente, un vehículo o una transacción.",
    verbose=True
)

# Agente 2: Recuperador jerárquico
recuperador = Agent(
    role="Recuperador Jerárquico",
    goal="Navegar el árbol documental del parking para encontrar información precisa",
    tools=[hierarchical_tool],
    backstory="Especialista en búsqueda multinivel. Sabe navegar "
              "de empresa → parking → cliente → vehículo según la consulta.",
    verbose=True
)

# Agente 3: Generador de respuesta
generador = Agent(
    role="Generador de Respuesta",
    goal="Producir una respuesta clara usando el contexto recuperado",
    backstory="Redactor técnico con experiencia en atención al cliente "
              "de aparcamientos. Explica tarifas, políticas e incidencias "
              "de forma comprensible.",
    verbose=True
)

# Agente 4: Validador
validador = Agent(
    role="Validador de Respuestas",
    goal="Verificar que la respuesta es correcta según las fuentes documentales",
    backstory="Auditor senior de ParkingCorp. Comprueba que cada afirmación "
              "esté respaldada por la documentación del parking.",
    verbose=True
)

# Tareas secuenciales
t1 = Task(
    description="Clasifica la consulta: '{consulta}' en nivel: "
               "empresa, parking, cliente, vehiculo o transaccion",
    agent=clasificador,
    expected_output="Nivel identificado y breve justificación"
)

t2 = Task(
    description="Recupera información jerárquica para: '{consulta}' "
                "usando el nivel indicado",
    agent=recuperador,
    expected_output="Documentos recuperados con metadatos de nivel y "
                    "relación padre-hijo"
)

t3 = Task(
    description="Genera respuesta para '{consulta}' usando el contexto recuperado",
    agent=generador,
    expected_output="Respuesta estructurada citando fuentes"
)

t4 = Task(
    description="Valida la respuesta contra las fuentes documentales: '{consulta}'",
    agent=validador,
    expected_output="Validación: correcta, incompleta o incorrecta con evidencia"
)

crew = Crew(
    agents=[clasificador, recuperador, generador, validador],
    tasks=[t1, t2, t3, t4],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={
    "consulta": "¿Puede el cliente A entrar al Parking Centro con su abono Premium?"
})
```

### 2.4 Patrones de consulta multi-nivel

El sistema multi-agente maneja distintos tipos de consulta según los niveles implicados:

| Tipo | Ejemplo | Niveles | Estrategia |
|------|---------|---------|------------|
| **Intra-nivel** | "¿Cuál es la tarifa del Parking Norte?" | Parking (1) | Recuperación directa |
| **Inter-nivel** | "¿Puede el cliente A acceder al Parking Centro?" | Cliente + Parking + Empresa | Ascender a padre común y descender |
| **Transversal** | "¿Cuánto ha pagado el cliente A este mes?" | Cliente + Transacciones | Agregación de nodos hoja |
| **Incidente** | "El vehículo 1234ABC tiene una disputa de multa" | Vehículo + Transacciones | Recuperación por matrícula + estado |

**Multi-agente + Jerarquía**: el clasificador identifica qué patrón aplicar, el recuperador navega correctamente el árbol según ese patrón, y el validador verifica que la respuesta es coherente entre niveles.

### 2.5 Patrones de orquestación multi-agente (RA3e)

Resumen de los patrones que ya conoces de la teoría general de sistemas multi-agente, ahora aplicados al caso parking:

| Patrón | Descripción | Aplicación parking |
|--------|-------------|-------------------|
| **Supervisor** | Un agente supervisor delega a especialistas y consolida | Supervisor de consultas parking: decide si la pregunta va a tarifas, clientes o incidencias |
| **Secuencial** | Agentes en cadena: output de A → input de B → output de C | Clasificar → Recuperar → Generar → Validar (el que usamos en 2.3) |
| **Swarm** | Agentes autónomos sin jerarquía fija | Varios agentes exploran la documentación del parking en paralelo y compiten por la mejor respuesta |
| **Debate** | Agentes con perspectivas opuestas discuten hasta consenso | Agente a favor del cliente vs. agente a favor de la empresa deciden si una multa es válida |
| **Crew** | Equipo con roles fijos, objetivos compartidos y coordinación central | El equipo de 4 agentes de ParkingCorp (clasificador, recuperador, generador, validador) |

---

## 3. Conexión con el Stack

```
F3: MLflow → modelo de embeddings registrado y versionado
F4: Prefect → orquesta re-indexación periódica de la jerarquía documental
F5: FastAPI → sirve el endpoint /consultar con el sistema multi-agente
F6: CrewAI + LlamaIndex → agentes especializados sobre índice jerárquico
F7: Evidently → monitorea calidad de recuperación por nivel jerárquico
F8: Guardrails → protege contra respuestas que mezclen niveles incorrectamente
```

**Ollama como fallback local**: al igual que en el RAG tradicional, Ollama permite ejecutar los modelos de lenguaje localmente para los agentes:

```python
from crewai import LLM

llm_local = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0.7
)

# Usar el mismo LLM local para todos los agentes del parking
agentes = [
    clasificador, recuperador, generador, validador
]
for agente in agentes:
    agente.llm = llm_local
```

**Requisitos**: `ollama pull llama3.2` (o cualquier modelo compatible, ~3-7 GB RAM).

---

## Apéndice: Ejemplo Bonus — Debate con AutoGen

> **Bonus**: Este ejemplo es adicional al contenido principal. Si usas CrewAI en la práctica, este apéndice te muestra cómo implementar el patrón **Debate** con AutoGen para comparar enfoques.

AutoGen es especialmente útil cuando necesitas que múltiples perspectivas discutan un problema antes de llegar a una decisión. En el caso ParkingCorp, podemos usarlo para decidir si una disputa de multa debe resolverse a favor del cliente o de la empresa:

```python
# pip install pyautogen
import autogen

# Configurar LLM local (Ollama)
config_list = [
    {
        "model": "ollama/llama3.2",
        "base_url": "http://localhost:11434",
        "api_type": "ollama",
    }
]

llm_config = {"config_list": config_list, "temperature": 0.7}

# Agente a favor del cliente
defensor_cliente = autogen.AssistantAgent(
    name="Defensor_Cliente",
    llm_config=llm_config,
    system_message=(
        "Eres un defensor de los derechos del cliente en ParkingCorp. "
        "Conoces las políticas a fondo y buscas siempre el beneficio "
        "del cliente dentro de lo legal. Argumentas a su favor."
    ),
)

# Agente a favor de la empresa
defensor_empresa = autogen.AssistantAgent(
    name="Defensor_Empresa",
    llm_config=llm_config,
    system_message=(
        "Eres un representante de ParkingCorp que vela por el cumplimiento "
        "de las políticas. Conoces las normas y buscas aplicarlas "
        "rigurosamente para proteger los ingresos de la empresa."
    ),
)

# Moderador neutral
moderador = autogen.AssistantAgent(
    name="Moderador",
    llm_config=llm_config,
    system_message=(
        "Eres un moderador neutral. Escuchas los argumentos de ambos lados "
        "y produces una resolución final equilibrada basada en los hechos "
        "y las políticas de ParkingCorp."
    ),
)

# Usuario proxy (simula al cliente real)
usuario = autogen.UserProxyAgent(
    name="Cliente",
    human_input_mode="NEVER",
    code_execution_config=False,
)

# Iniciar el debate
mensaje = (
    "El vehículo 1234ABC estuvo estacionado 4 horas en el Parking Centro. "
    "El ticket muestra entrada a las 10:00 pero el cliente dice que entró "
    "a las 09:30 y que el lector de matrículas falló. La política dice "
    "que sin evidencia del sensor se aplica la hora del ticket. "
    "¿Debemos hacer una excepción?"
)

resultado = usuario.initiate_chat(
    moderador,
    message=mensaje,
    max_turn=6,
)
```

**Cuándo usar CrewAI vs AutoGen**:

| Situación | CrewAI | AutoGen |
|-----------|--------|---------|
| Flujo secuencial predecible | ✅ Ideal | ❌ Sobredimensionado |
| Debate entre perspectivas | ❌ No diseñado para ello | ✅ Ideal |
| Procesos empresariales fijos | ✅ Perfecto | ❌ Demasiado flexible |
| Exploración creativa | ❌ Rígido | ✅ Excelente |

---

## 4. Resumen y Claves

1. **El RAG plano tiene limitaciones** con documentos estructurados jerárquicamente: pérdida de contexto, granularidad incorrecta y ruido en recuperación.
2. **La indexación jerárquica** organiza documentos en árboles (empresa → parking → cliente → vehículo) que preservan las relaciones padre-hijo.
3. **LlamaIndex** proporciona `HierarchicalNodeParser` para construir el árbol y `RecursiveRetriever` para navegarlo eficientemente.
4. **Los sistemas multi-agente** se benefician de la indexación jerárquica: clasificación inteligente, recuperación contextual y validación multinivel.
5. **El caso ParkingCorp** demuestra cómo una empresa real con documentación jerárquica se beneficia de este enfoque frente al RAG plano.
6. **Conexión RA3e**: la toma de decisiones basada en datos se fortalece cuando los agentes navegan la jerarquía documental con conciencia del contexto completo, no solo de chunks aislados.
7. **Elige indexación jerárquica cuando** tengas relaciones padre-hijo entre documentos. Para documentos planos, el RAG tradicional sigue siendo la opción correcta.

**En la práctica F6**: Construirás un sistema multi-agente con CrewAI + LlamaIndex que clasifica consultas sobre un parking empresarial, recupera información de la jerarquía documental (empresa → parking → cliente → vehículo), genera respuestas y las valida contra las fuentes originales.
