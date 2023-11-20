from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['nombre_de_la_base_de_datos']
collection = db['palabras']

class Palabra:
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado

def agregar_palabra():
    palabra = input("Ingrese la palabra: ")
    significado = input("Ingrese el significado: ")

    nueva_palabra = Palabra(palabra=palabra, significado=significado)

    # Insertar la palabra en la colección
    collection.insert_one(nueva_palabra.__dict__)
    print("Palabra agregada exitosamente.")

if __name__ == "__main__":
    agregar_palabra()
