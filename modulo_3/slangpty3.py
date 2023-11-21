from pymongo import MongoClient

def conectar_bd():
    client = MongoClient('localhost', 27017)
    db = client['slang_panameno']
    collection = db['palabras']
    return client, collection

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

        client, collection = conectar_bd()
        nueva_palabra = {
            'palabra': palabra,
            'significado': significado
        }
        collection.insert_one(nueva_palabra)
        print(f"La palabra {palabra} ha sido agregada correctamente.")
    elif opcion == 'c':
        palabra_a_editar = input("Ingrese la palabra que desea editar: ")
        nueva_palabra = input("Nueva palabra: ")
        nuevo_significado = input(f"Nuevo significado de {nueva_palabra}: ")

        client, collection = conectar_bd()
        query = {'palabra': palabra_a_editar}
        new_values = {'$set': {'palabra': nueva_palabra, 'significado': nuevo_significado}}
        collection.update_one(query, new_values)
        print("Palabra editada correctamente.")
    elif opcion == 'd':
        palabra_a_eliminar = input("Ingrese la palabra que desea eliminar: ")

        client, collection = conectar_bd()
        collection.delete_one({'palabra': palabra_a_eliminar})
        print(f"La palabra {palabra_a_eliminar} ha sido eliminada correctamente.")
    elif opcion == 'e':
        client, collection = conectar_bd()
        palabras = collection.find()

        if not palabras:
            print("El diccionario está vacío.")
        else:
            for palabra in palabras:
                print(f"{palabra['palabra']}: {palabra['significado']}")
    elif opcion == 'f':
        palabra_a_buscar = input("Que palabra desea buscar: ")

        client, collection = conectar_bd()
        palabra = collection.find_one({'palabra': palabra_a_buscar})

        if palabra:
            print(f"Significado de '{palabra_a_buscar}' es: {palabra['significado']}")
        else:
            print(f"La palabra {palabra_a_buscar} no se encuentra en el diccionario.")
    elif opcion == 'g':
        print("Hasta luego")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")