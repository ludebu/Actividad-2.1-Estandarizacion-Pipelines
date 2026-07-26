"""
Archivo: train.py

Este módulo realiza el procesamiento final de los datos
preparados. En esta primera entrega no se entrena un modelo
de Machine Learning, sino que se genera un resumen del
conjunto de datos.
"""


def procesar_datos(datos):
    """
    Muestra un resumen sencillo del dataset.
    """

    # Calcula el número total de registros.
    total_registros = len(datos)

    # Inicializa un diccionario para contar las especies.
    especies = {}

    # Recorre cada registro del dataset.
    for fila in datos:

        especie = fila["species"]

        # Cuenta cuántas veces aparece cada especie.
        if especie in especies:
            especies[especie] += 1
        else:
            especies[especie] = 1

    # Muestra los resultados.
    print("\n========== RESUMEN DEL DATASET ==========")
    print(f"Total de registros: {total_registros}")

    print("\nCantidad de registros por especie:")

    for especie, cantidad in especies.items():
        print(f"- {especie}: {cantidad}")

    print("\nProcesamiento finalizado correctamente.")
