# Estandarización de Pipelines y Control de Calidad de Datos

## Descripción

En esta actividad desarrollé un pipeline básico para trabajar con el dataset Iris. La idea principal fue organizar el proceso en varias etapas, comenzando por la carga de los datos, continuando con la validación de su calidad y finalizando con una preparación y un procesamiento sencillo del conjunto de datos.

Uno de los aspectos más importantes del ejercicio fue trabajar con un contrato de datos en formato JSON. En este archivo se definieron las reglas que debe cumplir el dataset, como las columnas esperadas, los tipos de datos, los rangos permitidos y las categorías válidas. De esta forma, las validaciones no quedaron escritas directamente en el código, sino que pueden modificarse desde un único archivo.

Todo el desarrollo se realizó en Visual Studio Code utilizando únicamente módulos estándar de Python, siguiendo las indicaciones dadas para la actividad.

---

## Objetivo

Construir un pipeline modular que permita:

- Cargar un archivo en formato CSV.
- Validar la estructura del dataset.
- Identificar valores vacíos.
- Verificar que los tipos de datos sean correctos.
- Validar rangos y categorías utilizando un contrato de datos.
- Preparar la información antes de su procesamiento.
- Generar un resumen básico del conjunto de datos.

---

## Estructura del proyecto

```text
Actividad 2.1 Estandarización Pipelines
│
├── data
│   ├── iris.csv
│   └── iris_invalid.csv
│
├── evidencias
│
├── models
│
├── src
│   ├── prepare.py
│   ├── train.py
│   └── validate_data.py
│
├── tests
│   └── test_invalid_data.py
│
├── data_contract.json
├── README.md
├── requirements.txt
└── run_pipeline.py
```

---

## Descripción de los archivos

### `run_pipeline.py`

Es el punto de inicio del proyecto. Desde este archivo se ejecutan todas las etapas del pipeline en el orden establecido.

Las etapas son:

1. Carga del contrato de datos.
2. Carga del archivo CSV.
3. Validación de calidad.
4. Preparación de los datos.
5. Procesamiento del dataset.

---

### `src/validate_data.py`

En este archivo se encuentran las funciones encargadas de validar la información.

Las validaciones realizadas incluyen:

- Verificación de las columnas esperadas.
- Detección de valores vacíos.
- Comprobación de los tipos de datos.
- Validación de rangos numéricos.
- Verificación de categorías permitidas.

Las reglas utilizadas durante estas validaciones se obtienen directamente del archivo `data_contract.json`.

---

### `src/prepare.py`

Este archivo realiza una preparación básica de los datos.

Durante esta etapa las variables numéricas que inicialmente son leídas como texto se convierten al tipo `float`, permitiendo que puedan utilizarse posteriormente sin inconvenientes.

---

### `src/train.py`

Aunque el nombre del archivo hace referencia al entrenamiento, en esta actividad únicamente se realizó un procesamiento descriptivo del dataset.

El programa presenta:

- El número total de registros.
- La cantidad de registros correspondiente a cada especie del conjunto Iris.

No se implementó un modelo de Machine Learning porque el objetivo de esta práctica fue construir la estructura del pipeline y fortalecer el proceso de validación de datos.

---

### `data_contract.json`

Este archivo contiene el contrato de datos utilizado durante el proyecto.

En él se definieron:

- Las columnas esperadas.
- El tipo de dato de cada variable.
- Los campos obligatorios.
- Los valores mínimos y máximos permitidos.
- Las especies aceptadas.
- Un ejemplo de registro válido.
- Un ejemplo de registro inválido.

Centralizar estas reglas en un único archivo facilita el mantenimiento del proyecto y evita modificar el código cada vez que cambien las condiciones de validación.

---

### `tests/test_invalid_data.py`

Este archivo se utilizó para comprobar que las validaciones realmente funcionan.

Para ello se creó un dataset con errores intencionales, incluyendo valores vacíos, datos fuera de rango y una categoría no permitida. Al ejecutar la prueba, el sistema identificó correctamente cada uno de estos errores.

---

## Requisitos

Para el desarrollo de esta actividad no fue necesario instalar librerías adicionales.

Únicamente se utilizaron módulos incluidos en Python:

- `csv`
- `json`
- `pathlib`
- `sys`

---

## Ejecución del pipeline principal

Ubicándose en la carpeta principal del proyecto, ejecutar:

```bash
python run_pipeline.py
```

Al finalizar deberá aparecer un mensaje similar al siguiente:

```text
PIPELINE FINALIZADO CORRECTAMENTE
```

---

## Ejecución de la prueba con datos inválidos

Para comprobar el funcionamiento de las validaciones ejecutar:

```bash
python tests/test_invalid_data.py
```

El resultado esperado es:

```text
PRUEBA EXITOSA: LOS ERRORES FUERON DETECTADOS
```

---

## Resultados obtenidos

Después de realizar las pruebas fue posible verificar que el pipeline funciona correctamente cuando el dataset cumple todas las condiciones definidas en el contrato de datos.

De igual forma, al utilizar el archivo con errores, el sistema detectó correctamente valores vacíos, datos fuera de los rangos establecidos y categorías que no hacen parte del contrato.

Esto permitió comprobar que las validaciones implementadas responden adecuadamente tanto para datos correctos como para datos incorrectos.

---

## Conclusiones

Con esta actividad comprendí la importancia de organizar un proyecto mediante un pipeline compuesto por diferentes etapas, donde cada archivo cumple una función específica.

También entendí la utilidad de trabajar con un contrato de datos, ya que permite separar las reglas de validación de la lógica del programa. Esto hace que el proyecto sea más fácil de mantener y adaptar cuando cambian las condiciones de los datos.

Finalmente, considero que esta práctica constituye una buena base para actividades posteriores relacionadas con el preprocesamiento de datos y el desarrollo de modelos de aprendizaje automático.

---

## Autor

**Luz Aydde Bustamante Tamayo**

Especialización en Ciencia de Datos

Universidad Santo Tomás

2026