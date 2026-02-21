from conexion import *

class CClientes:   
    def ingresarClientes(nombres, apellidos, sexo):
        try:
           
           cone = CConexion.ConexionBaseDatos()
           cursor = cone.cursor()
           sql = "INSERT INTO usuarios VALUES (null, %s,%s, %s);" 
           #La variables tiene que ser una tupla (no tienen que cambiar los valores)
           #Como minima expresión es (valor,) la coma hace que sea una tupla
           #Las tuplas son listas inmutables, eso quiere decir que no se pueden modificar

           valores = (nombres, apellidos, sexo)
           cursor.execute = (sql,valores)
           cone.commit()
           print(cursor.rowcount, "Registro ingresado")
           cone.close()

        except mysql.connector.Error as error: 
           print("Error de ingreso de datos {}".format(error ))
    