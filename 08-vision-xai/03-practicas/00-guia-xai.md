# Semana 24 – Explicabilidad en modelos de Visión y NLP

## 🎯 Objetivos
- Comprender la importancia de la **explicabilidad (XAI)** en modelos de IA.
- Aplicar **LIME** y **SHAP** en NLP y datos tabulares.
- Usar **Grad-CAM** para visualizar regiones activadas en CNNs de visión.
- Evaluar ventajas y limitaciones de cada técnica.

---

## 📚 Contenidos principales
1. **Conceptos de XAI**
   - Diferencia entre modelos caja blanca y caja negra.
   - Casos de uso críticos: medicina, finanzas, justicia.

2. **Técnicas trabajadas**
   - **LIME** → explicaciones locales en modelos de texto.
   - **SHAP** → valores de Shapley para medir importancia de variables.
   - **Grad-CAM** → mapas de calor en CNNs para imágenes.

3. **Reflexión crítica**
   - Qué explican y qué no explican estas herramientas.
   - Riesgos de sobreinterpretar los resultados.

---

## 📂 Notebooks trabajados
- **84_lime_text** → Explicabilidad en NLP con LIME.
- **85_shap_tabular** → Importancia de variables en modelos tabulares con SHAP.
- **86_gradcam_cnn** → Mapas de calor de activaciones en CNNs con Grad-CAM.

Incluyen:
- Versión base.
- Versión con soluciones (con pruebas sintéticas mínimas).
- Versión con soluciones + autotests.

---

## 🛠️ Actividades prácticas
1. Explicar frases positivas y negativas con LIME y comparar.
2. Generar gráficos SHAP (`summary_plot`, `force_plot`) para el dataset tabular.
3. Probar Grad-CAM en imágenes reales y superponer mapas de calor.
4. Reflexionar: ¿aumenta la confianza del usuario al ver explicaciones?

---

## ✅ Evaluación (RA2 y RA3)
- **RA2.c**: Definición de técnicas de explicabilidad.
- **RA2.d**: Implementación en NLP, tabular y visión.
- **RA2.e**: Evaluación de resultados.
- **RA3.a**: Identificación de ventajas de integrar explicabilidad.

**Criterios de evaluación:**
- Aplicación correcta de LIME, SHAP y Grad-CAM.
- Interpretación coherente de resultados.
- Identificación de limitaciones y riesgos.
- Relación con aplicaciones reales (sanidad, finanzas, industria).

---

## 📌 Recursos recomendados
- [LIME: Local Interpretable Model-agnostic Explanations](https://arxiv.org/abs/1602.04938)
- [SHAP documentation](https://shap.readthedocs.io/en/latest/)
- [Grad-CAM original paper](https://arxiv.org/abs/1610.02391)
