import time


def mostrar_inventario(peliculas):
    """
    Muestra todas las películas en formato de tabla.
    """

    if not peliculas:
        print("\nNo hay películas registradas.")
        return

    print("\n" + "=" * 100)
    print("                    LISTA DE PELÍCULAS")
    print("=" * 100)

    print(
        f"{'Código':<10}"
        f"{'Título':<25}"
        f"{'Género':<20}"
        f"{'Año':<8}"
        f"{'Calif.':<8}"
        f"{'Estado':<15}"
    )

    print("-" * 100)

    for pelicula in peliculas:

        print(
            f"{pelicula['codigo']:<10}"
            f"{pelicula['nombre'][:23]:<25}"
            f"{pelicula['genero'][:18]:<20}"
            f"{pelicula['anio']:<8}"
            f"{pelicula['calificacion']:<8}"
            f"{pelicula['estado']:<15}"
        )

    print("=" * 100)


def agregar_pelicula(peliculas):
    """
    Agrega una nueva película a la lista.
    """

    print("\n========== AGREGAR PELÍCULA ==========")

    codigo = input("Código de la película: ").strip()

    if not codigo:
        print("Error: el código no puede estar vacío.")
        return

    # Validar que el código no esté repetido
    for pelicula in peliculas:

        if pelicula["codigo"].lower() == codigo.lower():
            print("Error: ese código ya existe.")
            return

    nombre = input("Título de la película: ").strip()

    if not nombre:
        print("Error: el título no puede estar vacío.")
        return

    genero = input("Género: ").strip()

    if not genero:
        print("Error: el género no puede estar vacío.")
        return

    try:
        anio = int(input("Año de estreno: "))

        if anio <= 0:
            print("Error: el año debe ser válido.")
            return

        calificacion = float(input("Calificación (0 a 10): "))

        if calificacion < 0 or calificacion > 10:
            print("Error: la calificación debe estar entre 0 y 10.")
            return

    except ValueError:
        print("Error: debes ingresar números válidos.")
        return

    print("\nEstado de la película:")
    print("1. Vista")
    print("2. Pendiente")

    estado_opcion = input("Selecciona una opción: ")

    if estado_opcion == "1":
        estado = "Vista"

    elif estado_opcion == "2":
        estado = "Pendiente"

    else:
        print("Error: opción de estado inválida.")
        return

    nueva_pelicula = {
        "codigo": codigo,
        "nombre": nombre,
        "genero": genero,
        "anio": anio,
        "calificacion": calificacion,
        "estado": estado
    }

    peliculas.append(nueva_pelicula)

    print("\nPelícula agregada correctamente.")
    time.sleep(1)


def buscar_pelicula(peliculas):
    """
    Busca una película por código o título.
    """

    print("\n========== BUSCAR PELÍCULA ==========")

    dato = input("Ingresa el código o título: ").strip().lower()

    if not dato:
        print("Error: debes ingresar un dato.")
        return

    encontrados = []

    for pelicula in peliculas:

        if (
            dato in pelicula["codigo"].lower()
            or dato in pelicula["nombre"].lower()
        ):
            encontrados.append(pelicula)

    if encontrados:
        mostrar_inventario(encontrados)

    else:
        print("No se encontró ninguna película.")


def editar_pelicula(peliculas):
    """
    Permite editar los datos de una película.
    """

    print("\n========== EDITAR PELÍCULA ==========")

    codigo = input("Código de la película: ").strip().lower()

    for pelicula in peliculas:

        if pelicula["codigo"].lower() == codigo:

            print("\nPelícula encontrada:")
            print("Título:", pelicula["nombre"])
            print("Género:", pelicula["genero"])
            print("Año:", pelicula["anio"])
            print("Calificación:", pelicula["calificacion"])
            print("Estado:", pelicula["estado"])

            print("\n¿Qué deseas editar?")
            print("1. Título")
            print("2. Género")
            print("3. Año")
            print("4. Calificación")
            print("5. Estado")

            opcion = input("Selecciona una opción: ")

            match opcion:

                case "1":
                    nuevo_nombre = input("Nuevo título: ").strip()

                    if nuevo_nombre:
                        pelicula["nombre"] = nuevo_nombre
                        print("Título actualizado.")

                    else:
                        print("Error: el título no puede estar vacío.")

                case "2":
                    nuevo_genero = input("Nuevo género: ").strip()

                    if nuevo_genero:
                        pelicula["genero"] = nuevo_genero
                        print("Género actualizado.")

                    else:
                        print("Error: el género no puede estar vacío.")

                case "3":
                    try:
                        nuevo_anio = int(input("Nuevo año: "))

                        if nuevo_anio > 0:
                            pelicula["anio"] = nuevo_anio
                            print("Año actualizado.")

                        else:
                            print("Error: año inválido.")

                    except ValueError:
                        print("Error: debes ingresar un número.")

                case "4":
                    try:
                        nueva_calificacion = float(
                            input("Nueva calificación (0 a 10): ")
                        )

                        if 0 <= nueva_calificacion <= 10:
                            pelicula["calificacion"] = nueva_calificacion
                            print("Calificación actualizada.")

                        else:
                            print("Error: calificación inválida.")

                    except ValueError:
                        print("Error: debes ingresar un número.")

                case "5":
                    print("1. Vista")
                    print("2. Pendiente")

                    estado = input("Selecciona una opción: ")

                    if estado == "1":
                        pelicula["estado"] = "Vista"
                        print("Estado actualizado.")

                    elif estado == "2":
                        pelicula["estado"] = "Pendiente"
                        print("Estado actualizado.")

                    else:
                        print("Error: opción inválida.")

                case _:
                    print("Opción inválida.")

            return

    print("No se encontró una película con ese código.")


def eliminar_pelicula(peliculas):
    """
    Elimina una película mediante su código.
    """

    print("\n========== ELIMINAR PELÍCULA ==========")

    codigo = input("Código de la película: ").strip().lower()

    for pelicula in peliculas:

        if pelicula["codigo"].lower() == codigo:

            print("Película encontrada:", pelicula["nombre"])

            confirmar = input("¿Deseas eliminarla? (s/n): ").lower()

            if confirmar == "s":

                peliculas.remove(pelicula)

                print("Película eliminada correctamente.")

            else:
                print("Operación cancelada.")

            return

    print("No se encontró una película con ese código.")


def mostrar_pendientes(peliculas):
    """
    Muestra las películas que aún no han sido vistas.
    """

    pendientes = []

    for pelicula in peliculas:

        if pelicula["estado"].lower() == "pendiente":
            pendientes.append(pelicula)

    if pendientes:

        print("\n========== PELÍCULAS PENDIENTES ==========")

        mostrar_inventario(pendientes)

    else:
        print("\nNo hay películas pendientes.")