# Compute Cloud para IA

## ¿Por qué usar cómputo en la nube?

El entrenamiento y la inferencia de modelos suelen requerir recursos difíciles de mantener en local:

- GPUs especializadas como A100 o H100.
- Escalado puntual para picos de trabajo.
- Entornos listos con drivers, CUDA y librerías.
- Pago por uso en lugar de compra de infraestructura.

## Modelos de servicio habituales

| Modelo | Qué ofrece | Ejemplos |
|--------|------------|----------|
| IaaS | Máquinas virtuales con control total | EC2, Compute Engine, Azure VM |
| Plataforma gestionada | Entrenamiento, notebooks y endpoints | SageMaker, Vertex AI, Azure ML |
| SaaS especializado | Entornos simplificados con GPU | Lambda Labs, Paperspace, RunPod |

---

## Proveedores principales

### AWS

| Servicio | Tipo | Uso principal |
|----------|------|---------------|
| EC2 | IaaS | Control total de la máquina |
| SageMaker | Gestionado | Entrenamiento, notebooks y despliegue |
| Batch / ECS / EKS | Infraestructura | Procesamiento y despliegue por contenedores |

### Google Cloud

| Servicio | Tipo | Uso principal |
|----------|------|---------------|
| Compute Engine | IaaS | Máquinas virtuales y GPUs |
| Vertex AI | Gestionado | Entrenamiento, notebooks y endpoints |
| Colab | SaaS | Experimentación rápida |

### Azure

| Servicio | Tipo | Uso principal |
|----------|------|---------------|
| Virtual Machines | IaaS | Control total de la máquina |
| Azure ML | Gestionado | Entrenamiento, despliegue y seguimiento |

---

## Plataformas especializadas en IA

### Lambda Labs

- Sencillo de usar.
- Precios competitivos en GPU.
- Bueno para prototipado rápido.

### Paperspace

- Notebooks y máquinas con GPU.
- Útil para docencia, pruebas y entrenamiento ligero.

### RunPod y Vast.ai

- Mercado de GPUs con precios variables.
- Interesante cuando el coste es la prioridad.
- Requiere más atención a disponibilidad y estabilidad.

### CoreWeave

- Infraestructura especializada en cargas de IA.
- Mejor encaje en despliegues o escalado más exigentes.

### Alternativas libres o gratuitas

| Opción | Tipo | Comentario |
|--------|------|------------|
| Google Colab | Gratuita con límites | Muy útil para empezar y para docencia |
| Kaggle Notebooks | Gratuita con límites | Buena para ejercicios y datasets públicos |
| JupyterHub autogestionado | Software libre | Permite montar un entorno docente propio |
| SkyPilot | Software libre | Orquesta recursos de nube y simplifica el uso de GPUs |

---

## Comparativa orientativa de coste

Los precios cambian con frecuencia según región, disponibilidad y tipo de instancia, así que conviene tratarlos como referencia aproximada.

| Proveedor | Tipo de recurso | Perfil de uso |
|-----------|------------------|---------------|
| EC2 / Compute Engine / Azure VM | VM con GPU | Máximo control, más configuración |
| SageMaker / Vertex AI / Azure ML | Trabajo gestionado | Menos gestión, más integración |
| Lambda Labs / Paperspace | GPU especializada | Arranque rápido y coste competitivo |
| RunPod / Vast.ai | Mercado de GPUs | Coste bajo con más variabilidad |

---

## Notebooks gestionados

| Servicio | Ventaja principal |
|----------|-------------------|
| SageMaker Studio | Integración con el ecosistema AWS |
| Vertex AI Workbench | Integración con servicios de GCP |
| Azure ML Notebooks | Integración con Azure ML |
| Gradient | Facilidad de uso |
| Colab | Entrada rápida para pruebas |
| Kaggle | Útil para ejercicios y datasets públicos |

Son apropiados para exploración, docencia y pruebas iniciales. Para producción suelen complementarse con jobs de entrenamiento y despliegue.

---

## Criterios para elegir

| Necesidad | Recomendación general |
|-----------|-----------------------|
| Empezar rápido | Colab, Kaggle, Paperspace |
| Producción gestionada | SageMaker, Vertex AI, Azure ML |
| Máximo control | EC2, Compute Engine, Azure VM |
| Coste ajustado | Lambda Labs, RunPod, Vast.ai |
| Integración con ecosistema Big Data | Databricks, EMR, Dataproc |
| Entorno gratuito para docencia | Colab o Kaggle |

---

## Aplicación al proyecto

Antes de elegir una plataforma de compute, conviene responder:

1. ¿El proyecto necesita GPU o basta con CPU?
2. ¿Se entrenará un modelo propio o solo se hará inferencia?
3. ¿Hace falta un entorno sencillo para clase o un flujo reproducible?
4. ¿Se integrará con almacenamiento, MLOps o servicios ya elegidos?
5. ¿Qué pesa más: coste, facilidad de uso o control técnico?

En muchos proyectos académicos basta con una solución sencilla y reproducible. Si el proyecto no requiere entrenamiento intensivo, puede no tener sentido pagar por GPUs de gama alta.

---

## Aspectos a vigilar

1. Coste de transferencia de datos entre regiones o servicios.
2. Disponibilidad limitada de GPUs populares.
3. Riesgo de depender de instancias interrumpibles o preemptibles.
4. Coste del almacenamiento asociado a notebooks, checkpoints y modelos.
5. Diferencia entre un entorno cómodo para experimentar y uno adecuado para producción.

---

## Fuentes recomendadas

- Documentación oficial de Amazon SageMaker y EC2.
- Documentación oficial de Vertex AI y Compute Engine.
- Documentación oficial de Azure ML y Azure Virtual Machines.
- Documentación oficial de Lambda Labs, Paperspace y RunPod.
- Documentación oficial de Google Colab y Kaggle Notebooks.
- Documentación oficial de JupyterHub y SkyPilot.
