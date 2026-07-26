"""
Archivo: prepare.py

Este módulo prepara los datos para que puedan ser
utilizados durante la ejecución del pipeline.

Convierte las variables numéricas de texto a tipo float.
"""


def preparar_datos(datos):
    """
    Convierte las columnas numéricas del dataset
    al tipo de dato float.
    """

    # Lista donde se almacenarán los datos preparados.
    datos_preparados = []

    # Recorre cada registro del dataset.
    for fila in datos:

        # Crea una copia para no modificar el registro original.
        nueva_fila = fila.copy()

        # Convierte las variables numéricas.
        nueva_fila["sepal_length"] = float(fila["sepal_length"])
        nueva_fila["sepal_width"] = float(fila["sepal_width"])
        nueva_fila["petal_length"] = float(fila["petal_length"])
        nueva_fila["petal_width"] = float(fila["petal_width"])

        # Guarda el registro convertido.
        datos_preparados.append(nueva_fila)

    print("Preparación de datos finalizada correctamente.")

    return datos_preparados
