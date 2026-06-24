# Sesión RAG_index - Alternativas a PageIndex

## Contexto
- Usuario busca alternativa a PageIndex.ai (cuota límite 1 crédito/página, $30/mes)
- Documentos: libros técnicos, papers de IA/ML/DL, PyTorch, Keras, etc.
- Tiene Ollama funcionando con modelos cloud (minimax-m2:cloud, nemotron-3-super)
- Ha probado TreeRAG + Ollama

## Alternativas encontradas

| Librería | Instalación | Indexing | Query | Notas |
|----------|-------------|----------|-------|-------|
| **TreeDex** | `pip install treedex` | 0 LLM si PDF tiene ToC | LLM | ⭐ Recomendada |
| **doctr** | `pip install doctr-index` | Determinista, sin LLM | - | Solo indexing |
| **treeRAG** | `pip install treerag` | Requiere LLM | LLM | Ya probada |
| **PageIndex self** | `git clone` | Requiere OpenAI | LLM | Repo pesado |

## Benchmarks

| Herramienta | Resultado |
|-------------|-----------|
| PageIndex | 98.7% (FinanceBench) |
| TreeDex | 60% hit, 60% recall, 2.3x más preciso que Vector RAG |

## Ejemplo TreeDex para clase

```python
from treedex import TreeDex, OllamaLLM

# Configurar LLM
llm = OllamaLLM(
    base_url="http://localhost:11434",
    model="minimax-m2:cloud"
)

# Indexar PDF
index = TreeDex.from_file("documento.pdf", llm=llm)

# Ver estructura
index.show_tree()

# Guardar índice
index.save("indice.json")

# Cargar y consultar
loaded = TreeDex.load("indice.json", llm=llm)
result = loaded.query("pregunta", agentic=True)
print(result.answer)
print(result.pages_str)
```

## Notas sobre modelos Ollama
- minimax-m2:cloud: funciona bien, formato correcto
- nemotron-3-super: todo en una línea, difícil de leer (problema del modelo)

## Próximos pasos
1. Probar TreeDex con PDF real
2. Preparar ejercicios para alumnos
3. Comparar resultados con PageIndex cloud

## Recursos
- TreeDex docs: https://mithun50.github.io/TreeDex/
- TreeDex GitHub: https://github.com/mithun50/TreeDex
- doctr PyPI: https://pypi.org/project/doctr-index/
- treeRAG PyPI: https://pypi.org/project/treerag/