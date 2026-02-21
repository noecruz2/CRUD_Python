import mysql.connector

class CConexion:

    def ConexionBaseDatos():

        try:
            conexion = mysql.connector.connect(user= 'root', password = 'Chivas123',
                                                    host='127.0.0.1',
                                                    database='clientesdb',
                                                    port='3306')
            print("Conexion correcta")

            return conexion
            
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))

            return conexion

CConexion.ConexionBaseDatos()