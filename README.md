# 🧠 Entrenamiento de modelos de Yolo - InterSystems 2025

Este repositorio contiene el trabajo realizado durante mi práctica profesional  en **InterSystems**, en el año **2025** con el entrenamiento de varios modelos de Yolo en la detección de objetos

## 🧩 Descripción General

Este repositorio fue creado para documentar y que el usuario pueda replicar tareas similares o de mejoría en el entrenamiento de modelos

El enfoque principal fue trabajar en tareas relacionadas con:
- **Creación de Datasets**
    - **Población del dataset con imágenes personales**
    - **Población del dataset con imágenes en linea mediante busqueda en SPARQL**
    - **Utilización de Datasets publicos**
    - **Limpieza de Datasets**
    - **Labeling de imágenes**
- **Entrenamiento de Modelos a partir de los dataset**
    - **Selección de versión de modelo(v8, v11, v11s, v11m, etc)**
    - **Estudio y seleccion de hiperparametros para el entrenamiento**
    - **Estudio de rendimiento de modelos**



## 📁 Estructura del Repositorio

```bash
📦 ModelosYolo
├── 📦AgeAndGender/
│   └── informes, bitácoras, presentaciones
├── 📦GunAndKnife/
│   └── flujos de datos, mapeos, componentes utilizados
├── 📦Person/
│   └── capturas de los tableros y reportes generados
├── 📦ScriptsUtiles/
│   └── scripts y fragmentos de código desarrollados o modificados
└── README.md
```


## 📘 Tutotial de para la creación de un modelo con un dataset con herramienta de labeling online ROBOFLOW

En el archivo tutotial.pdf se encuentra un paso a paso de las instrucciones para conformar un dataset con la estructura necesaria para entrenar un modelo.

Este tutorial utiliza la herramienta Roboflow, la cual es una pagina web para cargar tus imágenes y labelearlas a mano una por una.

Tambien tiene un enlace a un google colab donde fueron entrendos gran partes de los modelos. Se ocupó colab puesto que este nos entrega una GPU de 16GB con 4 horas de procesamiento a la semana, lo que cumple con los recursos necesarios para poder generar el modelo.

## 💾 Creación de modelo a partir de Dataset en local

Otra variante para el entrenamiento fue la utilización de datasets comprimidos en .zip en local, para luego subirlos a drive para su utilización nuevamente en google colab.

La estructura necesaria para la aceptación del dataset es la siguiente:

```bash
📁 dataset/
├── 📁 images/
│   ├── 📁 train/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   ├── 📁 val/
│   │   ├── img3.jpg
│   │   ├── img4.jpg
│
├── 📁 labels/
│   ├── 📁 train/
│   │   ├── img1.txt
│   │   ├── img2.txt
│   ├── 📁 val/
│   │   ├── img3.txt
│   │   ├── img4.txt
│
├── data.yaml
```

Adjunto el colab correspondiente que se utilizó para estos modelos, el cual es una variante del tutorial anteriormente visto, aplicando descompresión y montado del dataset.

[Colab entrenamiento con dataset en .zip](https://colab.research.google.com/drive/1FdZxznTcUulnncZjtXq8TfpoUQUqbybX?usp=sharing)


## 📊 Visualización de un dataset

Para visualizar un dataset y poder analizar sus anotaciones y estructura se utiliza [Ultralytics HUB](https://hub.ultralytics.com/), que esta desarrollado directamente por los creadores de YOLO, aqui se puede recorrer las imagenes con sus boxes graficados y asi poder fijarse si existe algun labeling mal asignado.

**NOTA:** Para subir tu dataset aqui es neceario que el archivo .yaml y que la carpeta del dataset tengan el mismo nombre
