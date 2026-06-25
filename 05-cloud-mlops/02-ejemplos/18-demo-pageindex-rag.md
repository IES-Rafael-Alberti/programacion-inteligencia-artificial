# Demo técnica: RAG con PageIndex sin chunking clásico

## Objetivo

Esta demo está pensada para mostrar una alternativa al RAG clásico cuando trabajamos con documentos largos o muy estructurados. En lugar de trocear el documento en fragmentos y guardarlos en una base vectorial, `PageIndex` construye un índice jerárquico del documento y recupera contexto respetando mejor su estructura.

No busca sustituir la demo de RAG sencillo. Busca complementar esa demo para que el alumnado vea cuándo el `chunking` puede quedarse corto.

## Qué enseña

- Que no todo RAG tiene que basarse en `chunking + embeddings + base vectorial`.
- Cómo cambia el flujo cuando el documento se trata como una estructura.
- Cuándo puede tener sentido una herramienta como `PageIndex`.
- Cómo obtener respuestas con trazabilidad por página o sección.

## Qué no enseña

- Despliegue en producción.
- Evaluación sistemática de recuperación.
- Comparativas de rendimiento.
- Integraciones avanzadas con agentes.

---

## Idea de clase

Después de enseñar `15-demo-rag-sencillo.md`, se puede plantear esta pregunta:

"¿Qué pasa si el documento es largo, tiene secciones claras y una respuesta depende de mantener el contexto completo de una parte del texto?"

Ahí encaja esta demo.

---

## Flujo conceptual

```text
Documento largo -> índice jerárquico -> recuperación guiada por estructura -> contexto relevante -> respuesta con citas
```

Frente al flujo habitual:

```text
Documento -> fragmentación -> embeddings -> índice vectorial -> recuperación -> LLM -> respuesta
```

---

## Cuándo usar esta demo

- Cuando ya se ha explicado el RAG básico.
- Cuando se quiere mostrar una limitación del `chunking`.
- Cuando el documento tiene capítulos, apartados o páginas con significado propio.
- Cuando interesa justificar respuestas con referencias documentales.

## Cuándo no hace falta

- Si la clase solo necesita una primera toma de contacto con RAG.
- Si los documentos son pequeños y simples.
- Si no se quiere depender de una API externa en esa sesión.

---

## Requisitos previos

- Tener una cuenta y clave API de `PageIndex` si se quiere ejecutar en directo.
- Tener un PDF o documento largo con estructura clara.
- Tener instalado el SDK de Python.

Instalación orientativa:

```bash
pip install pageindex
```

---

## Documento recomendado para la demo

Conviene usar un documento donde se note bien la estructura, por ejemplo:

- una memoria de proyecto,
- un informe técnico,
- una normativa,
- un manual extenso en PDF.

Si el documento es demasiado corto, la diferencia respecto al RAG con fragmentos será menos visible.

---

## Guion de la demo

### Paso 1. Recordar el límite del RAG clásico

Explicar algo como:

"En el RAG básico partimos el texto en trozos. Eso funciona muchas veces, pero a veces rompe una explicación, una tabla, una conclusión o una sección importante."

### Paso 2. Presentar la alternativa

Explicar que `PageIndex` intenta trabajar sobre la estructura del documento en vez de depender del troceado manual.

### Paso 3. Subir o indexar el documento

Mostrar que el documento se envía al servicio para generar un índice navegable.

### Paso 4. Lanzar una pregunta

Ejemplos:

- "Resume las conclusiones principales del informe."
- "¿Qué requisitos aparecen en la sección de evaluación?"
- "¿En qué página se describe el procedimiento de despliegue?"

### Paso 5. Mostrar la respuesta y las citas

Lo importante aquí no es solo la respuesta final, sino enseñar:

- qué parte del documento ha recuperado,
- si cita páginas o secciones,
- y por qué eso puede ser más útil que varios fragmentos sueltos.

### Paso 6. Comparar con la demo básica

Cerrar enlazando con `15-demo-rag-sencillo.md`:

- para documentos pequeños, el enfoque simple suele bastar,
- para documentos largos y estructurados, puede tener sentido explorar recuperación jerárquica.

---

## Código mínimo orientativo

Este ejemplo es intencionalmente corto. Puede variar según la versión del SDK, así que conviene contrastarlo con la documentación oficial de `PageIndex`.

```python
from pageindex import PageIndexClient

client = PageIndexClient(api_key=os.environ["PAGEINDEX_API_KEY"])

result = client.submit_document("./informe.pdf")
doc_id = result["doc_id"]

response = client.chat_completions(
    messages=[
        {
            "role": "user",
            "content": "Resume las conclusiones principales y cita las páginas relevantes"
        }
    ],
    doc_id=doc_id
)

print(response)
```

---

## Qué conviene enseñar en pantalla

1. El documento original.
2. La idea de que no se está haciendo `chunking` manual.
3. El código mínimo de indexación y consulta.
4. La respuesta final.
5. Las referencias a páginas o secciones, si aparecen.

---

## Alternativas añadidas al notebook

El notebook incluye ahora tres bloques para comparar enfoques sin quedarse atado a `PageIndex Cloud`.

### treeRAG

`treeRAG` indexa documentos como árboles y consulta usando un LLM compatible con LangChain, por ejemplo `Ollama`.

Encaja bien para clase porque:

- no requiere base de datos vectorial,
- se instala de forma sencilla,
- permite explicar recuperación estructural,
- y ya estaba parcialmente probado en el notebook.

### TreeDex

`TreeDex` es la alternativa recomendada para probar primero como sustituto práctico de `PageIndex` en esta demo.

La idea didáctica es:

```text
PDF -> árbol navegable -> selección de nodos con LLM -> respuesta con páginas o secciones
```

Frente a `PageIndex`, su ventaja principal es que puede probarse localmente con una instalación sencilla. Su punto débil es el mismo que otras herramientas jóvenes: la estabilidad puede depender mucho del PDF, de la tabla de contenidos y del modelo usado.

### GraphRAG

`GraphRAG` se ha añadido como contraste avanzado, no como sustituto directo.

Conviene dejar claro al alumnado que:

- construye grafos de entidades, relaciones y comunidades,
- está pensado para corpus más amplios,
- puede consumir muchas llamadas al LLM durante la indexación,
- y por defecto no representa exactamente la idea de "sin chunking ni vector DB".

Por tanto, para esta sesión `GraphRAG` sirve mejor para explicar otra familia de recuperación avanzada. Para reemplazar `PageIndex`, tienen más sentido `TreeDex` o `treeRAG`.

---

## Mensajes clave para verbalizar en clase

- El RAG clásico no es la única forma de recuperar contexto.
- La estructura del documento también puede ser una fuente de información.
- En documentos largos, mantener contexto puede importar más que recuperar trozos parecidos.
- Una herramienta más avanzada no siempre es mejor: depende del caso.

---

## Relación con esta unidad

Esta demo complementa directamente:

- [12-recuperacion-avanzada-rag.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/12-recuperacion-avanzada-rag.md)
- [15-demo-rag-sencillo.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/15-demo-rag-sencillo.md)
- [17-demo-rag-ollama.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/17-demo-rag-ollama.md)
- [18-demo-pageindex-rag.ipynb](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.ipynb)
- [18-demo-pageindex-rag.ipynb.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.ipynb.md)

Sirve especialmente bien como segunda demo o como cierre comparativo tras explicar el enfoque básico.

---

## Cierre recomendado

Terminar con dos preguntas:

1. ¿En vuestro proyecto bastaría el RAG sencillo?
2. ¿Qué tipo de documento justificaría probar una recuperación basada en estructura como `PageIndex`?
