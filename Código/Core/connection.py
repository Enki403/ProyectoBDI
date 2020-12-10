import mysql.connector

class ConnectionDB:
    def __init__(self,credentials):
        self.credentials = credentials

    def validateUser(self,name,password):
        isUser = False

        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        query = 'SELECT * FROM User'
        cursor.execute(query)


        for i in cursor:
            if((i[1] == name) and (i[2]== password)):
                isUser = True
        cnx.close()

        return isUser

    #Metodo para guardar todos los datos de la DB en un array de tuplas
    def executeQueryRead(self, query, parameters = ()):
        valuesReturn = []
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.execute(query,parameters)
        for x in cursor:
            valuesReturn.append(x)
        cnx.close()
        return valuesReturn

    # Este metodo se encarga de crear y eliminar usuarios
    def executeQueryWrite(self,query,parameters = ()):
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.execute(query,parameters)
        cnx.commit()
        cnx.close()

