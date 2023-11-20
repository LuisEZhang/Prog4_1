import sqlite3

conn = sqlite3.connect('sgc.db')

while True:
   print("\n====SGC=====")
   print("1. Eliminar")
   print("2. Crear")
   print("3. Buscar")
   print("4. Actualizar")
   print("5. Salir")
   print("0. Crear Base de Datos")
   print("999. PANICO")
   
   try:
      opcion = int(input("\nOpcion: "))
   except:
      opcion = 1000

   if opcion == 1:
      print("\nEliminar")
      while True:
         print("\n1. Eliminar producto")
         print("2. Eliminar proveedor")
         print("3. Eliminar distribuidor")
         print("4. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         
         if opcion == 1:
            cursor = conn.execute("SELECT ID, NOMBRE FROM PRODUCTO")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            try:
               por_eliminar = int(input("Inserte ID del PRODUCTO a borrar... "))
            except:
               por_eliminar = 999999
            conn.execute("DELETE FROM PRODUCTO WHERE ID = " + str(por_eliminar ))
            conn.commit()
         elif opcion == 2:
            cursor = conn.execute("SELECT ID, NOMBRE FROM PROVEEDORES")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            try:
               por_eliminar = int(input("Inserte ID del PROVEEDOR a borrar... "))
            except:
               por_eliminar = 999999
            conn.execute("DELETE FROM PROVEEDORES WHERE ID = " + str(por_eliminar ))
            conn.commit()
         elif opcion == 3:
            cursor = conn.execute("SELECT ID, NOMBRE FROM DISTRIBUIDORES")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            try:
               por_eliminar = int(input("Inserte ID del PROVEEDOR a borrar... "))
            except:
               por_eliminar = 999999
            conn.execute("DELETE FROM DISTRIBUIDORES WHERE ID = " + str(por_eliminar) )
            conn.commit()
         elif opcion == 4:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 2:
      print("\nCrear")
      while True:
         print("\n1. Crear producto")
         print("2. Crear proveedor")
         print("3. Crear distribuidor")
         print("4. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         if opcion == 1:
            id = input("ID?")
            nombre = input("Nombre?")
            tipo = input("Tipo?")
            cantidad = input("Cuantos?")
            conn.execute("INSERT INTO PRODUCTO(ID, NOMBRE, TIPO, CANTIDAD) VALUES("+id+", \""+nombre+"\", \""+tipo+"\", \""+cantidad+"\")")
            conn.commit()
         elif opcion == 2:
            id = input("ID?")
            nombre = input("Nombre?")
            ubicacion = input("Ubicacion?")
            clasificacion = input("Clasificacion?")
            conn.execute("INSERT INTO PROVEEDORES(ID, NOMBRE, UBICACION, CLASIFICACION) VALUES("+id+", \""+nombre+"\", \""+ubicacion+"\", \""+clasificacion+"\")")
            conn.commit()
         elif opcion == 3:
            id = input("ID?")
            nombre = input("Nombre?")
            ubicacion = input("Ubicacion?")
            clasificacion = input("Clasificacion?")
            conn.execute("INSERT INTO DISTRIBUIDORES(ID, NOMBRE, UBICACION, CLASIFICACION) VALUES("+id+", \""+nombre+"\", \""+ubicacion+"\", \""+clasificacion+"\")")
            conn.commit()
         elif opcion == 4:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 3:
      print("\nBuscar")
      while True:
         print("\n1. Buscar producto")
         print("2. Buscar proveedor")
         print("3. Buscar distribuidor")
         print("4. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         if opcion == 1:
            cursor = conn.execute("SELECT NOMBRE FROM PRODUCTO")
            #for row in cursor:
            #   print(str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3]))
            for row in cursor:
                print(str(row[0]))
         elif opcion == 2:
            cursor = conn.execute("SELECT NOMBRE FROM PROVEEDORES")
            for row in cursor:
                print(str(row[0]))
         elif opcion == 3:
            cursor = conn.execute("SELECT NOMBRE FROM DISTRIBUIDORES")
            for row in cursor:
                print(str(row[0]))
         elif opcion == 4:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 4:
      print("\nActualizar")
      while True:
         print("\n1. Actualizar producto")
         print("2. Actualizar proveedor")
         print("3. Actualizar distribuidor")
         print("4. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         if opcion == 1:
            cursor = conn.execute("SELECT ID, NOMBRE FROM PRODUCTO")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            por_actualizar = input("Inserte ID del PRODUCTO por actualizar... ")
            nuevo_nombre = input("Inserte el nuevo nombre del PRODUCTO... ")
            conn.execute('UPDATE PRODUCTO SET NOMBRE = "' + nuevo_nombre + '" WHERE ID = ' + por_actualizar)
            conn.commit()
         elif opcion == 2:
            cursor = conn.execute("SELECT ID, NOMBRE FROM PROVEEDORES")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            por_actualizar = input("Inserte ID del PROVEEDOR por actualizar... ")
            nuevo_nombre = input("Inserte el nuevo nombre del PROVEEDOR... ")
            conn.execute('UPDATE PROVEEDORES SET NOMBRE = "' + nuevo_nombre + '" WHERE ID = ' + por_actualizar)
            conn.commit()
         elif opcion == 3:
            cursor = conn.execute("SELECT ID, NOMBRE FROM DISTRIBUIDORES")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            por_actualizar = input("Inserte ID del DISTRIBUIDOR por actualizar... ")
            nuevo_nombre = input("Inserte el nuevo nombre del DISTRIBUIDOR... ")
            conn.execute('UPDATE DISTRIBUIDORES SET NOMBRE = "' + nuevo_nombre + '" WHERE ID = ' + por_actualizar)
            conn.commit()
         elif opcion == 4:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 5:
      break
   elif opcion == 0:
      print("\nCrear estructura de base de datos")
      conn.execute('''CREATE TABLE IF NOT EXISTS PROVEEDORES
                   (ID INT PRIMARY KEY NOT NULL,
                    NOMBRE TEXT NOT NULL,
                    UBICACION CHAR(50),
                    CLASIFICACION TEXT);''')
      conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCTO
                   (ID INT PRIMARY KEY NOT NULL,
                    NOMBRE TEXT NOT NULL,
                    TIPO TEXT,
                    CANTIDAD INT);''')
      conn.execute('''CREATE TABLE IF NOT EXISTS DISTRIBUIDORES
                   (ID INT PRIMARY KEY NOT NULL,
                    NOMBRE TEXT NOT NULL,
                    UBICACION TEXT,
                    CLASIFICACION TEXT);''')
     # conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCTO_TIENE_PROVEEDOR
     #              (PROD_ID INT NOT NULL,
     #               PROV_ID INT NOT NULL,
     #               CONSTRAINT PK_PTP
     #                 PRIMARY KEY (PROD_ID, PROV_ID),
     #               CONSTRAINT FK_PROD
     #                 FOREIGN KEY (PROD_ID)
     #                 REFERENCES PRODUCTO(ID),
     #               CONSTRAINT FK_PROV
     #                 FOREIGN KEY (PROV_ID)
     #                 REFERENCES PROVEEDORES(PROV_ID);''')
     # conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCTO_TIENE_DISTRIBUIDOR
     #              (PROD_ID INT NOT NULL,
     #               DIST_ID INT NOT NULL,
     #               CONSTRAINT PK_PTD
     #                 PRIMARY KEY (PROD_ID, DIST_ID),
     #               CONSTRAINT FK_PROD
     #                 FOREIGN KEY (PROD_ID)
     #                 REFERENCES PRODUCTO(ID),
     #               CONSTRAINT FK_DIST
     #                 FOREIGN KEY (DIST_ID)
     #                 REFERENCES DISTRIBUIDORES(DIST_ID);''')
   elif opcion == 999:
      secreto = "admin123"
      password = input("Password: ")
      if secreto == password:
          while True:
             opcion = input("¿Estas seguro (S/N)?")
             if opcion.upper() == "S":
                 print("BOOM!")
                 conn.execute("DELETE FROM PRODUCTO;")
                 conn.execute("DELETE FROM PROVEEDORES;")
                 conn.execute("DELETE FROM DISTRIBUIDORES;")
                 break
             else:
                 print("Se fue la DEA")
                 break
      else:
          print("Dale de aqui, payaso!")
   else:
      print("ERR::Opcion no valida")
