import redis

def conectar_bd():
    conexion = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
    return conexion

def editar_palabra(conexion, palabra_a_editar, nueva_palabra, nuevo_significado):
    if conexion.hexists("palabras", palabra_a_editar):
        conexion.hset("palabras", nueva_palabra, nuevo_significado)
        conexion.hdel("palabras", palabra_a_editar)
        print("Palabra editada correctamente.")
    else:
        print(f"La palabra {palabra_a_editar} no existe en el diccionario.")

def eliminar_palabra(conexion, palabra_a_eliminar):
    if conexion.hexists("palabras", palabra_a_eliminar):
        conexion.hdel("palabras", palabra_a_eliminar)
        print(f"La palabra {palabra_a_eliminar} ha sido eliminada correctamente.")
    else:
        print(f"La palabra {palabra_a_eliminar} no existe en el diccionario.")

conexion = conectar_bd()

while True:
    print("\nDSP")
    print("a) Agregar nueva palabra")
    print("c) Editar palabra existente")
    print("d) Eliminar palabra")
    print("e) Lista de palabras")
    print("f) Buscar significado de palabra")
    print("g) Salir")

    opcion = input("Que desea hacer?").lower()

    if opcion == 'a':
        palabra = input("Palabra: ")
        significado = input("Significado: ")
        conexion.hset("palabras", palabra, significado)
        print(f"La palabra {palabra} ha sido agregada correctamente.")

    elif opcion == 'c':
        palabra_a_editar = input("Ingrese la palabra que desea editar: ")
        nueva_palabra = input("Nueva palabra: ")
        nuevo_significado = input(f"Nuevo significado de {nueva_palabra}: ")
        editar_palabra(conexion, palabra_a_editar, nueva_palabra, nuevo_significado)

    elif opcion == 'd':
        palabra_a_eliminar = input("Ingrese la palabra que desea eliminar: ")
        eliminar_palabra(conexion, palabra_a_eliminar)

    elif opcion == 'e':
        palabras = conexion.hgetall("palabras")
        if not palabras:
            print("El diccionario está vacío.")
        else:
            for palabra, significado in palabras.items():
                print(f"{palabra}: {significado}")

    elif opcion == 'f':
        palabra_a_buscar = input("Que palabra desea buscar: ")
        significado = conexion.hget("palabras", palabra_a_buscar)
        if significado:
            print(f"Significado de '{palabra_a_buscar}' es: {significado}")
        else:
            print(f"La palabra {palabra_a_buscar} no se encuentra en el diccionario.")

    elif opcion == 'g':
        print("Hasta luego")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")
