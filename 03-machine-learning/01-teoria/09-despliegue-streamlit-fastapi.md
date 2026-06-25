# ⚖️ Streamlit vs FastAPI
## ¿Cuándo usar cada uno en proyectos de Inteligencia Artificial?

En los proyectos de IA es habitual **entrenar modelos correctamente**, pero también es clave **saber cómo exponerlos**.
Streamlit y FastAPI **no compiten**, sino que **resuelven problemas distintos**.

---

## 🧩 ¿Qué es Streamlit?

**Streamlit** es un framework orientado a la **creación rápida de aplicaciones web interactivas**, pensado principalmente para:

- Visualización de datos
- Demostraciones de modelos
- Prototipos rápidos
- Interfaces sencillas para usuarios no técnicos

👉 Convierte scripts de Python en apps web **sin necesidad de frontend**.

---

## 🧩 ¿Qué es FastAPI?

**FastAPI** es un framework para crear **APIs REST profesionales**, pensado para:

- Exponer modelos como servicios
- Integrarse con otros sistemas
- Producción real
- Arquitecturas backend modernas

👉 Es una API, **no una interfaz gráfica**.

---

## 🧠 Comparativa directa

| Aspecto | Streamlit | FastAPI |
|------|-----------|---------|
| Tipo | App web interactiva | API REST |
| Enfoque | Visualización / demo | Backend / producción |
| Entrada de datos | Formularios, sliders | JSON |
| Salida | Gráficas, texto, tablas | JSON |
| Validación | Básica | Fuerte (Pydantic) |
| Documentación automática | ❌ | ✅ (`/docs`) |
| Escalabilidad | Baja | Alta |
| Uso en producción | Limitado | Muy adecuado |
| Perfil ideal | Data Scientist | Ingeniero / Informático |

---

## 🎯 ¿Cuándo usar **Streamlit**?

Usa **Streamlit** cuando:

- Quieres **ver resultados rápidamente**
- Necesitas una **demo visual**
- El usuario es humano (profesor, cliente, alumno)
- El objetivo es explorar o explicar un modelo
- Estás en fase de **prototipo**

### Ejemplos
- App para predecir precios con sliders
- Dashboard de métricas
- Visualización interactiva de resultados
- Demostración de un proyecto final

---

## 🎯 ¿Cuándo usar **FastAPI**?

Usa **FastAPI** cuando:

- Necesitas un **servicio reutilizable**
- El consumidor es otro sistema (frontend, app, microservicio)
- Quieres **validación robusta**
- Necesitas escalabilidad
- Estás pensando en **producción real**

### Ejemplos
- API de predicción para una app web
- Backend para una app móvil
- Servicio de inferencia para otros módulos
- Arquitecturas tipo microservicios

---

## 🧱 Arquitectura típica combinando ambos

En proyectos reales **se usan juntos**:
Usuario
↓
Streamlit (UI)
↓ HTTP
FastAPI (API)
↓
Modelo de IA

- **Streamlit** → interfaz
- **FastAPI** → lógica y modelo

---

## 🧪 En este módulo (PIA)

### Uso recomendado

- **Streamlit**
  👉 Primer despliegue
  👉 Visualizar y entender el modelo

- **FastAPI**
  👉 Proyecto final
  👉 Evaluación profesional
  👉 Perfil informático

📌 En el proyecto final se acepta **uno de los dos**, pero:
- **FastAPI suma más valor técnico**
- Streamlit es válido si está bien justificado

---

## 🧠 Conclusión

> **Streamlit muestra modelos.
> FastAPI los sirve.**

Saber **cuándo usar cada uno** es tan importante como entrenar bien el modelo.
# ✅ Checklist de decisión — Despliegue del proyecto IA

Marca las casillas que se cumplan en tu proyecto.

---

## 🔹 Usa **Streamlit** si:

- ⬜ El usuario final es una persona (profesor, cliente, alumno)
- ⬜ Necesitas una **interfaz visual**
- ⬜ Quieres mostrar gráficos, tablas o explicaciones
- ⬜ El proyecto es una **demo o prototipo**
- ⬜ No necesitas integrarte con otros sistemas
- ⬜ El modelo se ejecuta solo bajo demanda
- ⬜ Buscas rapidez y simplicidad

👉 **Resultado recomendado:** Streamlit

---

## 🔹 Usa **FastAPI** si:

- ⬜ El consumidor del modelo es otro software
- ⬜ Necesitas enviar y recibir datos en JSON
- ⬜ Quieres validación estricta de entrada
- ⬜ El modelo debe reutilizarse en varios contextos
- ⬜ Piensas en producción real
- ⬜ Necesitas escalar o contenerizar (Docker)
- ⬜ Quieres documentación automática (`/docs`)

👉 **Resultado recomendado:** FastAPI

---

## 🔹 Usa **Streamlit + FastAPI** si:

- ⬜ Quieres interfaz + backend profesional
- ⬜ El modelo debe estar desacoplado de la UI
- ⬜ Simulas una arquitectura real
- ⬜ Buscas la máxima nota técnica

👉 **Resultado recomendado:** Arquitectura combinada

---

## ⚠️ Importante para la evaluación

- Streamlit **es válido**
- FastAPI **tiene mayor peso técnico**
- La elección debe **justificarse**
