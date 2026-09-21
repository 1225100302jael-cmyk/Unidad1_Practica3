import time

from datos import cargar_datos, guardar_datos

from operaciones import (
    mostrar_inventario,
    agregar_pelicula,
    buscar_pelicula,
    editar_pelicula,
    eliminar_pelicula,
    mostrar_pendientes
)


def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """

    print("\n" + "═" * 50)
    print("       🎬 SISTEMA DE GESTIÓN DE PELÍCULAS 🎬")
    print("═" * 50)

    print("1. Agregar película")
    print("2. Mostrar todas las películas")
    print("3. Buscar película")
    print("4. Editar película")
    print("5. Eliminar película")
    print("6. Mostrar películas pendientes")
    print("7. Guardar y salir")
    print("8. Salir sin guardar")

    print("═" * 50)


def main():
    """
    Función principal del programa.
    """

    # Cargar las películas al iniciar
    peliculas = cargar_datos()

    print("\nBienvenido al sistema de películas.")
    print(f"Se cargaron {len(peliculas)} películas.")

    time.sleep(1)

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opción: ").strip()

        match opcion:

            case "1":
                agregar_pelicula(peliculas)

                guardar_datos(peliculas)

            case "2":
                mostrar_inventario(peliculas)

            case "3":
                buscar_pelicula(peliculas)

            case "4":
                editar_pelicula(peliculas)

                guardar_datos(peliculas)

            case "5":
                eliminar_pelicula(peliculas)

                guardar_datos(peliculas)

            case "6":
                mostrar_pendientes(peliculas)

            case "7":
                guardar_datos(peliculas)

                print("Gracias por utilizar el sistema.")
                print("Programa finalizado.")

                break

            case "8":
                print("Saliendo sin guardar cambios...")
                break

            case _:
                print("Error: opción inválida.")

        time.sleep(1)


if __name__ == "__main__":
    main()