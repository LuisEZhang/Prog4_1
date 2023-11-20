from pymongo import MongoClient

def conectar_bd():
    client = MongoClient('localhost', 27017)
    db = client['slang_panameno']
    collection = db['palabras']
    return client, collection

def agregar_palabra():
    palabra = input("Palabra: ")
    significado = input("Significado: ")

    client, collection = conectar_bd()
    nueva_palabra = {
        'palabra': palabra,
        'significado': significado
    }
    collection.insert_one(nueva_palabra)
    print(f"La palabra {palabra} ha sido agregada correctamente.")

def editar_palabra():
    palabra_a_editar = input("Ingrese la palabra que desea editar: ")
    nueva_palabra = input("Nueva palabra: ")
    nuevo_significado = input(f"Nuevo significado de {nueva_palabra}: ")

    client, collection = conectar_bd()
    query = {'palabra': palabra_a_editar}
    new_values = {'$set': {'palabra': nueva_palabra, 'significado': nuevo_significado}}
    collection.update_one(query, new_values)
    print("Palabra editada correctamente.")

def eliminar_palabra():
    palabra_a_eliminar = input("Ingrese la palabra que desea eliminar: ")

    client, collection = conectar_bd()
    collection.delete_one({'palabra': palabra_a_eliminar})
    print(f"La palabra {palabra_a_eliminar} ha sido eliminada correctamente.")

def ver_listado():
    client, collection = conectar_bd()
    palabras = collection.find()

    if not palabras:
        print("El diccionario está vacío.")
    else:
        for palabra in palabras:
            print(f"{palabra['palabra']}: {palabra['significado']}")

def buscar_significado():
    palabra_a_buscar = input("Que palabra desea buscar: ")

    client, collection = conectar_bd()
    palabra = collection.find_one({'palabra': palabra_a_buscar})

    if palabra:
        print(f"Significado de '{palabra_a_buscar}' es: {palabra['significado']}")
    else:
        print(f"La palabra {palabra_a_buscar} no se encuentra en el diccionario.")

def menu():
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
            agregar_palabra()
        elif opcion == 'c':
            editar_palabra()
        elif opcion == 'd':
            eliminar_palabra()
        elif opcion == 'e':
            ver_listado()
        elif opcion == 'f':
            buscar_significado()
        elif opcion == 'g':
            print("Hasta luego")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()