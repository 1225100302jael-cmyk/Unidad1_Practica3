import json

# Nombre del archivo donde se guardan las películas
ARCHIVO_DATOS = "peliculas.json"


def cargar_datos():
    """
    Carga las películas desde el archivo JSON.
    """

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            # Validar que el contenido sea una lista
            if not isinstance(datos, list):
                print("Error: el archivo no contiene una lista.")
                return []

            return datos

    except FileNotFoundError:
        print("Aviso: no se encontró el archivo.")
        print("Se iniciará con una lista vacía.")
        return []

    except json.JSONDecodeError:
        print("Error: el archivo JSON está dañado o vacío.")
        return []

    except Exception as error:
        print(f"Error inesperado: {error}")
        return []


def guardar_datos(peliculas):
    """
    Guarda las películas en el archivo JSON.
    """

    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:

            json.dump(
                peliculas,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("Datos guardados correctamente.")

    except Exception as error:
        print(f"Error al guardar los datos: {error}")