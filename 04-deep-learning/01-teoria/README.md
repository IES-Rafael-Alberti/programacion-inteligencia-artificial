# UD4 · Modelado Avanzado de Redes Neuronales

Módulo de **Programación de Inteligencia Artificial** — IES Rafael Alberti 2025/26.

---

## Estructura del directorio

```
15-ModeladoAvanzadoDeRedesNeuronales/
│
├── entornos/                         Scripts de instalación de entornos conda/pip
│   ├── environment.yml
│   ├── install_jax.sh
│   ├── install_keras3.sh
│   ├── install_mlx.sh
│   ├── install_onnx.sh
│   ├── install_pytorch.sh
│   └── install_tensorflow.sh
│
├── docs/
│   ├── frameworks/                   Guías y tutoriales por framework
│   │   ├── 001-DeepLearning_{JAX,Keras3,MLX,ONNX,PyTorch,TensorFlow}.md
│   │   ├── ArquitecturaRedConvolucionalMaxPoolFiltros.md
│   │   ├── {keras,pytorch,tensorflow}_tutorial.pdf
│   │   └── tutorial_{keras2,keras3,pytorch}.org
│   ├── conceptos/                    Conceptos fundamentales de DL
│   │   ├── NLP_Atencion.md
│   │   ├── RedesConvolucionales.md
│   │   ├── RedesRecurrentes.md
│   │   ├── TensorFlow_BajoNivel.md
│   │   ├── TensorFlow_DataAPI.md
│   │   └── tf_df_imgs.md
│   ├── metricas/                     Métricas, funciones de pérdida, sobreajuste
│   │   ├── 002-MetricasPytorchKeras.{md,pdf}
│   │   ├── 003-MetricasRegresion.{md,pdf}
│   │   ├── Curva-Precision_Recall.{md,html,pdf}
│   │   ├── lossfunctions.pdf
│   │   ├── SaturacionFuncionActivacionSigmoide.png
│   │   ├── SesgoVarianzaEn-ML.jpeg
│   │   ├── Sobreajuste-Subajuste_En-ML.jpeg
│   │   ├── Underfit_JustRight_Overfit.png
│   │   └── Underfit-Overfit_BiasVariance.html
│   ├── teoria/                       Documentación teórica general
│   │   ├── 001-ChatGPT-GradDesc-Backprop.{md,pdf}
│   │   ├── 001-DeepLearningV{1,2}.{md,org,tex}
│   │   ├── 002-Comparativa_Frameworks.md
│   │   ├── 002-Underfit-Overfit_BiasVariance.md
│   │   ├── AjusteDeHiperParametros.org
│   │   ├── DeepLearningV2.tex
│   │   ├── GeneracionNumerAleatorios.org
│   │   ├── GUIA_PROYECTO_PYTHON_ML.{md,html}
│   │   ├── LSTM.{org,tex}
│   │   ├── notas_housing.txt
│   │   ├── planTrabajoPytorch.txt
│   │   ├── RESUMEN_TRABAJO.md
│   │   └── TensorFlowPlayGround.{org,pdf,tex}
│   └── libros/                       Libros de referencia (PDF/EPUB)
│       ├── 001-DeepLearningV{1,2}.pdf
│       ├── AprendizajeProfundoIntroUtilizandoPython.pdf
│       ├── Deep Learning with Python (beginners guide).pdf
│       ├── Deep Reinforcement Learning with Python (2024).pdf
│       ├── DeepLearningforCoderswithfastai...{pdf,epub}
│       ├── DeepL-s11277-022-10079-4.pdf
│       ├── Hands-OnMachineLearning...{2022,3rdEd}.pdf
│       ├── LongShort-TermMemoryNetworksWithPython-2017.pdf
│       ├── LSTM.pdf
│       ├── Mastering_NLP_from_Foundations_to_LLMs...pdf
│       ├── Natural Language Processing {and IR, in Action, with PyTorch, Understanding}.pdf
│       ├── Natural_Language_Understanding_with_Python...pdf
│       └── Rothman_Transf_for_Nat_Lang_Proc_2021.pdf
│
├── proyectos/
│   ├── boston-housing/               Predicción precio viviendas Boston
│   │   ├── data/housing.csv
│   │   ├── docs/{BostonHousing-1.md, -2.md, BostonHousingDesc.txt}
│   │   ├── notebooks/nna-vs-traditional.ipynb
│   │   └── scripts/bostonHousesPrice_{Keras,Pytorch,SciKeras,SciPytorch}.py
│   ├── house-prices-kaggle/          Kaggle House Prices (regresión avanzada)
│   │   ├── data/{train,test,sample_submission}.csv + extras + .zip
│   │   ├── notebooks/{house_prices_advanced_regresionR,regression2,prueba}.ipynb
│   │   └── docs/{rubrica.md, rubricaSelecEntrenModel.odt, conceptos.org}
│   ├── used-cars/                    Predicción precio coches de segunda mano
│   │   ├── data/{usedCars.zip, vehicles.zip}
│   │   ├── extras/Samoyedo.jpg
│   │   ├── mlruns/
│   │   └── notebooks/{keras_notebook2,layersReuse,pytorch_notebook,tf_keras_notebook,vehiculoPycaret}.ipynb
│   └── euromillones/                 Predicción Euromillones con LSTM
│       ├── data/{Euromillones.csv, Euromillones-result.csv}
│       ├── notebooks/{euromill-boosting,euromillions-3,euromill-premio,euromPytorch}.ipynb
│       └── scripts/{LSTM-euromillions,LSTM_PytorchMultiVariate,LSTM_PytorchUniVariate}.py
│
├── tareas/                           Enunciados de tareas y ejercicios
│   ├── 3-Tarea_RNN_SeriesTemporales.md
│   ├── CasoPracticoTF_KerasFlask.org
│   ├── Tarea_BlackFriday.md
│   ├── TareaCNN_vision.md
│   ├── TareaNLP-DL.md
│   └── clasificacion/
│       ├── EjercicioClasificacionANN.{md,org,pdf}
│       ├── EjercicioClasificacionANN-Solucion.org
│       └── EjerciciosClasificacion.org
│
├── datos/
│   └── blackfriday/                  Dataset Black Friday
│       ├── blkfri_train.csv
│       └── blkfri_test.csv
│
├── notebooks/                        Notebooks didácticos generales
│   ├── fundamentos/                  Ejemplos básicos por framework
│   │   ├── 01_Ejemplo_Keras3.ipynb
│   │   ├── 02_Ejemplo_PyTorch.ipynb
│   │   ├── 03_Ejemplo_JAX_Flax.ipynb
│   │   ├── 04_Ejemplo_TensorFlow.ipynb
│   │   ├── TF_data_API.ipynb
│   │   └── tf-playground-datasets.ipynb
│   ├── series-temporales/
│   │   └── RNN_SeriesTemporales.ipynb
│   └── vision/
│       ├── Clasificacion_Tumores_ResNet18.ipynb
│       ├── CNN_visionV2.ipynb
│       ├── Deteccion_Objetos_FasterRCNN.ipynb
│       ├── Deteccion_Objetos_FasterRCNN_Lote.ipynb
│       └── tf_df_imgs.ipynb
│
├── vision/                           Visión por computador
│   ├── teoria/                       Teoría: notebooks 01-13 + dlib + guías
│   │   ├── 01-Introduccion_Vision_Por_Computador.ipynb
│   │   ├── ...
│   │   ├── 13-Ejemplo_Proyecto_Kather_Clasificacion_Tejidos.ipynb
│   │   ├── dlib_facial_landmarks.ipynb
│   │   ├── dlib_opencv_landmarks.py
│   │   ├── environment.yml
│   │   ├── Guia_Profesor_Vision.{md,pdf}
│   │   ├── Notebooks_Vision_Por_Computador.zip
│   │   ├── shape_predictor_68_face_landmarks.dat.bz2
│   │   └── VisionX_computadorGuiaProfesor.md
│   ├── yolo/                         Materiales YOLO v11
│   │   ├── comprueba_paquete_conda.sh
│   │   ├── Guia_Profesor_Vision_Actualizada.md
│   │   ├── Guia_Profesor_Vision_IA_YOLOv11.docx
│   │   ├── YOLOv11_Deteccion_Notebook.zip
│   │   ├── YOLOv11_Pose_Notebook.zip
│   │   └── YOLOv11_Segmentacion_Notebook.zip
│   └── datos/
│       └── imagenes_ejemplo_deteccion.zip
│
├── nlp/                              Procesamiento de Lenguaje Natural
│   ├── docs/                         Documentación NLP general
│   │   ├── 001-Keras-NLP.{md,pdf}
│   │   ├── 001-Pytorch-NLP.{md,pdf}
│   │   └── 002-NLP-Embeddings.{md,html,pdf}
│   ├── datos/
│   │   ├── el_quijote.txt
│   │   └── CREA_total.zip
│   ├── libros/                       (vacío — libros NLP movidos a docs/libros/)
│   └── transformers/
│       ├── docs/                     Documentación Transformers (md, html, PNG, PDF)
│       │   ├── 003-Transformers-{0,I,II,III,IV,V,VI}.{md,html}
│       │   ├── 003-Transformers-0.pdf
│       │   ├── Codificacion_Posicional_Transformer.pdf
│       │   └── *.png  (8 imágenes de arquitectura)
│       ├── notebooks/                10 notebooks de Transformers/BERT/Atención
│       ├── datos/
│       │   ├── mini_qa_dataset.tsv
│       │   ├── mini_trad_es_en{,_ampliado}.tsv
│       │   └── squad_es_mini.json
│       ├── tareas/                   Enunciados, rúbricas, test Moodle
│       │   ├── Ejercicios_Atencion_Cross.pdf
│       │   ├── Ejercicios_Codificacion_Posicional.pdf
│       │   ├── Entrega_Transformer_Traductor.pdf
│       │   ├── Rubrica_{BERT_QA,Transformer_Traductor}.pdf
│       │   └── Transformers_Test_Moodle.gift
│       ├── modelos/
│       │   └── transformer_model.pth
│       ├── scripts/
│       │   └── transformerPytorch.py
│       └── zips/
│           ├── Proyecto_BERT_QA.zip
│           ├── Proyecto_Transformer_Traductor.zip
│           └── Transformers.zip
│
└── ejemplos/                         Aplicaciones de ejemplo completas
    ├── PIA_S15 Codigo Fuente.zip
    └── fashion-mnist-flask/          App Flask + Keras para clasificación Fashion-MNIST
        ├── README.txt
        └── fashion-mnist/
            ├── application.py
            ├── train.py
            ├── requirements.txt
            ├── model/fashion_mnist/  (modelo Keras guardado)
            └── img/{dress.png, t-shirt.png, data.zip}
```

---

## Notas

- Los **libros NLP** se centralizan en `docs/libros/` junto al resto de libros de Deep Learning.
- El fichero `nlp/datos/el_quijote.txt` es la copia única (el duplicado en `nlp/transformers/` era idéntico y se eliminó).
- `nlp/libros/` queda vacío (placeholder) porque los libros se consolidaron en `docs/libros/`.
- Los archivos temporales eliminados: `.Rhistory`, `logs.log`, `.unison.*.tmp`, `__pycache__/`, `_minted-*/`, `.idea/`, `.vscode/`, directorios vacíos de Housing.
