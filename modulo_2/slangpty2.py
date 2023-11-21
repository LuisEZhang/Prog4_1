import mysql.connector

DB_CONFIG = {
    'host': 'ingresar host',
    'user': 'su usuario',
    'password': 'su contraseña',
    'database': 'su base de datos',
}

def conectar_bd():
    conexion = mysql.connector.connect(**DB_CONFIG)
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INT AUTO_INCREMENT PRIMARY KEY,
            palabra VARCHAR(255),
            significado TEXT
        )
    ''')

    conexion.commit()
    return conexion, cursor


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

        conexion, cursor = conectar_bd()
        cursor.execute("INSERT INTO palabras (palabra, significado) VALUES (%s, %s)", (palabra, significado))
        conexion.commit()
        print(f"La palabra {palabra} ha sido agregada correctamente.")

    elif opcion == 'c':
        palabra_a_editar = input("Ingrese la palabra que desea editar: ")
        nueva_palabra = input("Nueva palabra: ")
        nuevo_significado = input(f"Nuevo significado de {nueva_palabra}: ")

        conexion, cursor = conectar_bd()
        cursor.execute("UPDATE palabras SET palabra=%s, significado=%s WHERE palabra=%s",
                       (nueva_palabra, nuevo_significado, palabra_a_editar))
        conexion.commit()
        print("Palabra editada correctamente.")

    elif opcion == 'd':
        palabra_a_eliminar = input("Ingrese la palabra que desea eliminar: ")

        conexion, cursor = conectar_bd()
        cursor.execute("DELETE FROM palabras WHERE palabra=%s", (palabra_a_eliminar,))
        conexion.commit()
        print(f"La palabra {palabra_a_eliminar} ha sido eliminada correctamente.")

    elif opcion == 'e':
        conexion, cursor = conectar_bd()
        cursor.execute("SELECT palabra, significado FROM palabras")
        palabras = cursor.fetchall()

        if not palabras:
            print("El diccionario está vacío.")
        else:
            for palabra, significado in palabras:
                print(f"{palabra}: {significado}")

    elif opcion == 'f':
        palabra_a_buscar = input("Que palabra desea buscar: ")

        conexion, cursor = conectar_bd()
        cursor.execute("SELECT significado FROM palabras WHERE palabra=%s", (palabra_a_buscar,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"Significado de '{palabra_a_buscar}' es: {resultado[0]}")
        else:
            print(f"La palabra {palabra_a_buscar} no se encuentra en el diccionario.")

    elif opcion == 'g':
        print("Hasta luego")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")