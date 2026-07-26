# Importamos Path para construir rutas independientes
# del sistema operativo.
from pathlib import Path

# Importamos las funciones responsables de cargar y validar los datos.
from src.validate_data import (
    cargar_contrato,
    cargar_datos,
    validar_columnas,
    validar_nulos,
    validar_tipos,
    validar_rangos
)

# Importamos la función de preparación del dataset.
from src.prepare import preparar_datos

# Importamos la función de procesamiento.
from src.train import procesar_datos


def ejecutar_pipeline():
    """
    Ejecuta de manera ordenada todas las etapas del pipeline
    para el dataset Iris.
    """

    print("=" * 60)
    print("INICIO DEL PIPELINE DEL DATASET IRIS")
    print("=" * 60)

    # Obtenemos la carpeta raíz donde se encuentra este archivo.
    carpeta_proyecto = Path(__file__).parent

    # Construimos la ruta del archivo CSV.
    ruta_datos = carpeta_proyecto / "data" / "iris.csv"

    # Construimos la ruta del contrato de datos.
    ruta_contrato = carpeta_proyecto / "data_contract.json"

    # ----------------------------------------------------------
    # ETAPA 1: CARGA DEL CONTRATO
    # ----------------------------------------------------------

    print("\nETAPA 1: Carga del contrato de datos")

    contrato = cargar_contrato(ruta_contrato)

    # Si el contrato no puede cargarse, el pipeline se detiene.
    if contrato is None:
        print("\nPIPELINE DETENIDO: No fue posible cargar el contrato.")
        return

    # ----------------------------------------------------------
    # ETAPA 2: CARGA DE DATOS
    # ----------------------------------------------------------

    print("\nETAPA 2: Carga de datos")

    datos = cargar_datos(ruta_datos)

    # Si los datos no pueden cargarse, el pipeline se detiene.
    if datos is None:
        print("\nPIPELINE DETENIDO: No fue posible cargar los datos.")
        return

    # ----------------------------------------------------------
    # ETAPA 3: VALIDACIÓN DE CALIDAD
    # ----------------------------------------------------------

    print("\nETAPA 3: Validación de calidad")

    columnas_validas = validar_columnas(datos, contrato)
    nulos_validos = validar_nulos(datos, contrato)
    tipos_validos = validar_tipos(datos, contrato)
    rangos_validos = validar_rangos(datos, contrato)

    # Reunimos el resultado de todas las validaciones.
    validaciones = [
        columnas_validas,
        nulos_validos,
        tipos_validos,
        rangos_validos
    ]

    # all() devuelve True únicamente cuando todas las validaciones
    # son correctas.
    if not all(validaciones):
        print("\nPIPELINE DETENIDO: El dataset no cumple el contrato.")
        return

    # ----------------------------------------------------------
    # ETAPA 4: PREPARACIÓN DE DATOS
    # ----------------------------------------------------------

    print("\nETAPA 4: Preparación de datos")

    datos_preparados = preparar_datos(datos)

    # ----------------------------------------------------------
    # ETAPA 5: PROCESAMIENTO DE DATOS
    # ----------------------------------------------------------

    print("\nETAPA 5: Procesamiento de datos")

    procesar_datos(datos_preparados)

    # ----------------------------------------------------------
    # FINALIZACIÓN
    # ----------------------------------------------------------

    print("\n" + "=" * 60)
    print("PIPELINE FINALIZADO CORRECTAMENTE")
    print("=" * 60)


# Este bloque garantiza que el pipeline se ejecute únicamente
# cuando este archivo se inicia directamente.
if __name__ == "__main__":
    ejecutar_pipeline()