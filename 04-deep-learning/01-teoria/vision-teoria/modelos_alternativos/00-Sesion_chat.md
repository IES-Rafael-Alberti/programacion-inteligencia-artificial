# Sesión de Chat: Creación de Material Didáctico - Modelos Alternativos a Transformers
## UD4 · Modelado Avanzado

---

## 📅 Fecha: 14 de abril de 2026

---

## 🗨️ Conversación

### Mensaje inicial del usuario:
> mira el fichero LFM_version_profesor.md, LFM_version_profesor.md y LFM_quijote_comparativa.ipynb, vamos a crear la versión para el alumno de los liquid foundation models; para los transformers hice una implementación de cero en pytorch, pero creo que no sería necesario llegar a tanto en este caso, y en el notebook lo he implementando usando capas preparadas de pytorch

### Respuesta:
Se crearon los archivos LFM_version_alumno.ipynb y LFM_version_alumno.md con:
- Explicaciones paso a paso más guiadas
- Código extensamente comentado
- Ejercicios integrados
- Preguntas de reflexión
- Experimentos opcionales

---

### Mensaje del usuario:
> habría que hacer lo mismo para modelos tipo mamba, tenía un documento de una conversación con lo que habría que hacer, pero no lo encuentro ; así que toca hacerlo de cero, el del profe y el del alumno

### Respuesta:
Se crearon 4 archivos para Mamba:
- Mamba_quijote_comparativa.ipynb (versión profesor)
- Mamba_version_alumno.ipynb
- Mamba_version_profesor.md
- Mamba_version_alumno.md

El MambaBlock implementado incluye:
- Proyección de entrada
- Convolución local (d_conv=4)
- SSM scan con selección de B, C, dt dependientes del input
- Gate de salida y skip connection
- RMSNorm

---

### Mensaje del usuario:
> crea un documento comparando transformers, liquid models y mamba (o ssm en general), ventajs, inconventientes de cada uno, ejemplos típicos de uso, por qué en unas tareas es mejor escoger un modelo en lugar de otro... también si hay alguna otra arquitectura que veas relevante para la comparativa añádela

### Respuesta:
Se creó Arquitecturas_comparativa.md con:
- Comparativa general con gráficos ASCII
- Análisis detallado de Transformers, Liquid Models, Mamba
- 5 arquitecturas adicionales: LSTM/GRU, RWKV, RetNet, Hyena, gMLP
- Tabla comparativa completa (complejidad, memoria, paralelismo)
- Decision tree para elegir arquitectura
- Matriz de decisión por escenario
- Línea temporal evolutiva
- Frases mnemotécnicas

---

### Mensaje del usuario:
> crea una carpeta para meter todo lo generado, algo así como modelos_alternativos o similar; una vez echa la carpeta mete los docuemntos y notebooks que has generado, los de mamba, los de liquied y lod de rwkv

### Respuesta:
Se creó la carpeta modelos_alternativos/ y se movieron todos los archivos. También se crearon los materiales de RWKV:
- RWKV_quijote_comparativa.ipynb
- RWKV_version_alumno.ipynb
- RWKV_version_profesor.md
- RWKV_version_alumno.md

RWKV implementado con:
- RWKVTimeMix (attention-like con decay)
- RWKVChannelMix (FFN-like con gate)
- Time shift para contexto local
- Estado persistente para inferencia O(1)

---

### Mensaje del usuario:
> para los transformers hice 4 ejemplos de uso, uno de traducción(transformer completo encoder-decoder para seq2seq) inglés español con un pequeño vocabulario de unas 100 palabras y frases comunes (un tsv); otro ejemplo decoder-only para generar texto partiendo de un pequeñoo conjunto de frases del quijote; otro ejemplo encoder only en el que se le daban unas frases y su etiqueta diciendo el tipo de frase: afirmación, pregunta o saludo, y al darle una frase la tenía que clasificar en una de esas categorías; el otro ejemplo otro seq2seq (transformer completo encoder´-decoder) en el que aprende frases y a reformularlas con sinónimos o frases parecidas (también tsv), los datos están en /home/jmsa/IESRafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD4/04-modelado-avanzado/nlp/transformers/datos/mini_clasificacion_intenciones.tsv, los ejemplos están en /home/jmsa/IESRafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD4/04-modelado-avanzado/nlp/transformers/scripts/, crea esos ejemplos para mamba y lfm

### Respuesta:
Se crearon scripts_mamba/ y scripts_lfm/ con los 4 ejemplos cada uno:

**Mamba scripts:**
1. ejemplo_mamba_1_traduccion_en_es.py (Seq2Seq)
2. ejemplo_mamba_2_generacion_decoder_only.py (Generación)
3. ejemplo_mamba_3_clasificacion_intenciones.py (Clasificación)
4. ejemplo_mamba_4_reformulacion.py (Seq2Seq)

**LFM scripts:**
1. ejemplo_lfm_1_traduccion_en_es.py (Seq2Seq)
2. ejemplo_lfm_2_generacion_decoder_only.py (Generación)
3. ejemplo_lfm_3_clasificacion_intenciones.py (Clasificación)
4. ejemplo_lfm_4_reformulacion.py (Seq2Seq)

Cada uno con su módulo base (mamba_blocks.py, lfm_blocks.py) conteniendo:
- Encoder-Decoder para Seq2Seq
- Decoder-Only para Generación
- Encoder-Only para Clasificación

---

### Mensaje del usuario:
> se pidió sobre transformers unas tareas que están en /home/jmsa/IESRafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD4/04-modelado-avanzado/nlp/transformers/, la idea ahora es que cojan alguna de esas tareas , las repliquen con mamba y lfm (ideal grupos de 2 y cada uno hace un modelo) y comparen con transformer, en eficacia, tiempo de entrenamiento, tiempo de inferencias, etc.; crea una tarea para esa comparativa

### Respuesta:
Se crearon:
1. **01-Practica_Comparativa.md** - Guía completa de la práctica
   - Tareas disponibles
   - Métricas a recopilar
   - Rúbrica de evaluación
   - Preguntas de análisis
   - Consejos

2. **02-Plantilla_Informe.md** - Plantilla para el informe de los alumnos

3. **metricas.py** - Script para recopilar métricas de entrenamiento e inferencia

4. **comparativa.py** - Script completo que entrena los 3 modelos y genera gráficos comparativos

5. Se copiaron los datos a modelos_alternativos/datos/

---

### Mensaje del usuario:
> ¿todo terminado?

### Respuesta:
Sí, se confirmó que todo estaba terminado.

---

### Mensaje del usuario:
> perfecto, guarda todo lo hecho en un fichero y la sesión

### Respuesta:
Se crearon:
1. **00-README.md** - Resumen completo del proyecto
2. **00-Sesion_chat.md** - Este documento con la transcripción de la sesión

---

## 📊 Archivos totales creados: 34

- Documentación: 12 archivos .md
- Scripts Python: 11 archivos
- Notebooks: 6 archivos .ipynb
- Datos: 7 archivos
- README: 2 archivos

---

## ✅ Checklist final

- [x] Carpetas creadas (modelos_alternativos/, scripts_mamba/, scripts_lfm/, datos/)
- [x] Material Mamba (notebooks, scripts, docs)
- [x] Material LFM (notebooks, scripts, docs)
- [x] Material RWKV (notebooks, docs)
- [x] Comparativa de arquitecturas
- [x] 4 ejemplos completos (Mamba y LFM)
- [x] Práctica de comparativa
- [x] Métricas y scripts de análisis
- [x] Datos compartidos
- [x] Documentación resumen
- [x] Transcripción de sesión

---

*Sesión guardada el 14 de abril de 2026*
