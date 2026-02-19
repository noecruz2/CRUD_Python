import mysql.connector

class CConexion

    def ConexionBaseDatos():

        try:
            conexion = mysql.connector.connect(user= '', password = ''
                                               )
            
        except mysql.connector.Error as error
            print("Error al conectarte a la base de datos {}".fotmat(error))