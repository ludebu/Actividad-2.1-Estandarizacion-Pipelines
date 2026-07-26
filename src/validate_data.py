# Importamos el módulo csv para leer archivos en formato CSV.
import csv

# Importamos json para leer el contrato de datos.
import json

# Importamos Path para manejar las rutas de los archivos.
from pathlib import Path


def cargar_contrato(ruta_contrato):
    """
    Carga el contrato de datos almacenado en formato JSON.

    Parámetros:
        ruta_contrato: ubicación del archivo data_contract.json.

    Retorna:
        Un diccionario con las reglas definidas en el contrato.
    """

    # Convertimos la ruta recibida en un objeto Path.
    ruta = Path(ruta_contrato)

    # Verificamos que el archivo exista.
    if not ruta.exists():
        print(f"ERROR: No se encontró el contrato de datos: {ruta}")
        return None

    try:
        # Abrimos el archivo JSON en modo lectura.
        with open(ruta, mode="r", encoding="utf-8") as archivo:

            # Convertimos el contenido JSON en un diccionario de Python.
            contrato = json.load(archivo)

        print("Contrato de datos cargado correctamente.")
        return contrato

    except json.JSONDecodeError:
        # Este error aparece cuando el JSON tiene problemas de sintaxis.
        print("ERROR: El contrato de datos no tiene un formato JSON válido.")
        return None


def cargar_datos(ruta_archivo):
    """
    Carga los datos del archivo CSV.

    Parámetros:
        ruta_archivo: ubicación del archivo iris.csv.

    Retorna:
        Una lista de diccionarios, donde cada diccionario representa una fila.
    """

    # Convertimos la ruta en un objeto Path.
    ruta = Path(ruta_archivo)

    # Comprobamos que el archivo exista.
    if not ruta.exists():
        print(f"ERROR: No se encontró el archivo: {ruta}")
        return None

    # Abrimos el archivo CSV.
    with open(ruta, mode="r", encoding="utf-8") as archivo:

        # DictReader utiliza los encabezados como nombres de las columnas.
        lector = csv.DictReader(archivo)

        # Convertimos todas las filas en una lista.
        datos = list(lector)

    print(
        f"Archivo cargado correctamente. "
        f"Registros encontrados: {len(datos)}"
    )

    return datos


def validar_columnas(datos, contrato):
    """
    Verifica que las columnas del CSV coincidan con las definidas
    en el contrato de datos.
    """

    # Verificamos que existan registros para analizar.
    if not datos:
        print("ERROR: No existen datos para validar.")
        return False

    # Obtenemos las columnas esperadas desde el contrato JSON.
    columnas_esperadas = set(contrato["columns"].keys())

    # Obtenemos las columnas que realmente tiene el CSV.
    columnas_reales = set(datos[0].keys())

    # Comparamos ambos conjuntos de columnas.
    if columnas_reales == columnas_esperadas:
        print("VALIDACIÓN CORRECTA: Las columnas coinciden.")
        return True

    # Identificamos las columnas faltantes.
    columnas_faltantes = columnas_esperadas - columnas_reales

    # Identificamos las columnas adicionales.
    columnas_adicionales = columnas_reales - columnas_esperadas

    print("ERROR DE VALIDACIÓN: Las columnas no coinciden.")

    if columnas_faltantes:
        print(f"Columnas faltantes: {columnas_faltantes}")

    if columnas_adicionales:
        print(f"Columnas adicionales: {columnas_adicionales}")

    return False


def validar_nulos(datos, contrato):
    """
    Comprueba que las columnas obligatorias no tengan valores vacíos.
    """

    errores = []

    # Recorremos cada registro del dataset.
    for numero_fila, fila in enumerate(datos, start=2):

        # Recorremos las columnas definidas en el contrato.
        for columna, reglas in contrato["columns"].items():

            # Consultamos si la columna es obligatoria.
            es_obligatoria = reglas.get("required", False)

            # Obtenemos el valor registrado en la columna.
            valor = fila.get(columna)

            # Validamos que un campo obligatorio no esté vacío.
            if es_obligatoria and (
                valor is None or str(valor).strip() == ""
            ):
                errores.append(
                    f"Fila {numero_fila}: valor vacío en '{columna}'."
                )

    # Si se encontraron errores, los mostramos.
    if errores:
        print("ERROR DE VALIDACIÓN: Se encontraron valores vacíos.")

        for error in errores:
            print(f"- {error}")

        return False

    print("VALIDACIÓN CORRECTA: No se encontraron valores vacíos.")
    return True


def validar_tipos(datos, contrato):
    """
    Verifica que cada valor pueda convertirse al tipo definido
    en el contrato de datos.
    """

    errores = []

    # Recorremos las filas del dataset.
    for numero_fila, fila in enumerate(datos, start=2):

        # Recorremos las columnas y sus reglas.
        for columna, reglas in contrato["columns"].items():

            # Obtenemos el tipo esperado.
            tipo_esperado = reglas.get("type")

            # Obtenemos el valor del registro.
            valor = fila.get(columna)

            # Los valores vacíos ya se revisan en validar_nulos.
            if valor is None or str(valor).strip() == "":
                continue

            try:
                # Si el contrato indica float, intentamos convertir a decimal.
                if tipo_esperado == "float":
                    float(valor)

                # Si el contrato indica integer, intentamos convertir a entero.
                elif tipo_esperado == "integer":
                    int(valor)

                # Si el contrato indica string, comprobamos que sea texto.
                elif tipo_esperado == "string":
                    str(valor)

                else:
                    errores.append(
                        f"Fila {numero_fila}: tipo no reconocido "
                        f"para '{columna}': {tipo_esperado}."
                    )

            except ValueError:
                errores.append(
                    f"Fila {numero_fila}: el valor '{valor}' de "
                    f"'{columna}' no corresponde al tipo "
                    f"'{tipo_esperado}'."
                )

    if errores:
        print("ERROR DE VALIDACIÓN: Se encontraron tipos incorrectos.")

        for error in errores:
            print(f"- {error}")

        return False

    print("VALIDACIÓN CORRECTA: Los tipos de datos son adecuados.")
    return True


def validar_rangos(datos, contrato):
    """
    Valida los rangos numéricos y los valores permitidos definidos
    en el contrato de datos.
    """

    errores = []

    # Recorremos todas las filas.
    for numero_fila, fila in enumerate(datos, start=2):

        # Recorremos las reglas de cada columna.
        for columna, reglas in contrato["columns"].items():

            valor = fila.get(columna)
            tipo_esperado = reglas.get("type")

            # Ignoramos valores vacíos porque fueron revisados anteriormente.
            if valor is None or str(valor).strip() == "":
                continue

            # Validación para columnas numéricas.
            if tipo_esperado in ("float", "integer"):

                try:
                    numero = float(valor)
                except ValueError:
                    # El error de tipo ya es informado por validar_tipos.
                    continue

                # Obtenemos el valor mínimo del contrato.
                minimo = reglas.get("minimum")

                # Obtenemos el valor máximo del contrato.
                maximo = reglas.get("maximum")

                if minimo is not None and numero < minimo:
                    errores.append(
                        f"Fila {numero_fila}: '{columna}' tiene el "
                        f"valor {numero}, inferior al mínimo {minimo}."
                    )

                if maximo is not None and numero > maximo:
                    errores.append(
                        f"Fila {numero_fila}: '{columna}' tiene el "
                        f"valor {numero}, superior al máximo {maximo}."
                    )

            # Validación para columnas con una lista de valores permitidos.
            valores_permitidos = reglas.get("allowed_values")

            if valores_permitidos is not None:
                if valor not in valores_permitidos:
                    errores.append(
                        f"Fila {numero_fila}: el valor '{valor}' de "
                        f"'{columna}' no está permitido."
                    )

    if errores:
        print(
            "ERROR DE VALIDACIÓN: Existen valores fuera de los "
            "rangos o categorías permitidas."
        )

        for error in errores:
            print(f"- {error}")

        return False

    print(
        "VALIDACIÓN CORRECTA: Los valores están dentro de los rangos."
    )
    return True
