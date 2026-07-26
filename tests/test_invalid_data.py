# Importamos sys para configurar el acceso a los módulos del proyecto.
import sys

# Importamos Path para construir las rutas de los archivos.
from pathlib import Path


# Obtenemos la carpeta raíz del proyecto.
# El archivo de prueba está dentro de tests, por eso usamos parent.parent.
carpeta_proyecto = Path(__file__).parent.parent

# Agregamos la carpeta raíz al buscador de módulos de Python.
# Esto permite importar correctamente el contenido de src.
sys.path.append(str(carpeta_proyecto))


# Importamos las funciones de carga y validación.
from src.validate_data import (
    cargar_contrato,
    cargar_datos,
    validar_columnas,
    validar_nulos,
    validar_tipos,
    validar_rangos
)


def probar_dataset_invalido():
    """
    Ejecuta las validaciones sobre un archivo que contiene errores
    intencionales, con el propósito de comprobar que el pipeline
    los identifica correctamente.
    """

    print("=" * 60)
    print("PRUEBA DE CONTROL CON DATASET INVÁLIDO")
    print("=" * 60)

    # Construimos la ruta del contrato de datos.
    ruta_contrato = carpeta_proyecto / "data_contract.json"

    # Construimos la ruta del archivo que contiene errores.
    ruta_datos_invalidos = (
        carpeta_proyecto / "data" / "iris_invalid.csv"
    )

    # Cargamos el contrato de datos.
    contrato = cargar_contrato(ruta_contrato)

    # Detenemos la prueba si el contrato no se pudo cargar.
    if contrato is None:
        print("PRUEBA DETENIDA: No fue posible cargar el contrato.")
        return

    # Cargamos el dataset inválido.
    datos = cargar_datos(ruta_datos_invalidos)

    # Detenemos la prueba si el archivo no se pudo cargar.
    if datos is None:
        print("PRUEBA DETENIDA: No fue posible cargar los datos.")
        return

    print("\nRESULTADOS DE LAS VALIDACIONES")

    # Ejecutamos cada una de las validaciones.
    columnas_validas = validar_columnas(datos, contrato)
    nulos_validos = validar_nulos(datos, contrato)
    tipos_validos = validar_tipos(datos, contrato)
    rangos_validos = validar_rangos(datos, contrato)

    # Agrupamos los resultados obtenidos.
    resultados = [
        columnas_validas,
        nulos_validos,
        tipos_validos,
        rangos_validos
    ]

    # El archivo fue diseñado para fallar.
    # Por eso, la prueba es exitosa cuando alguna validación devuelve False.
    if not all(resultados):
        print("\n" + "=" * 60)
        print("PRUEBA EXITOSA: LOS ERRORES FUERON DETECTADOS")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("ADVERTENCIA: EL ARCHIVO INVÁLIDO NO FUE RECHAZADO")
        print("=" * 60)


# Ejecutamos la prueba cuando se inicia directamente este archivo.
if __name__ == "__main__":
    probar_dataset_invalido()
