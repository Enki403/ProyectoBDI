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


    def executeQueryRead(self, query, parameters = ()):
        valuesReturn = []
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.execute(query,parameters,multi=True)
        for x in cursor:
            valuesReturn.append(x)
                
        cnx.close()

        return valuesReturn


    def executeQueryWrite(self,query,parameters = ()):
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.execute(query,parameters)
        cnx.commit()
        cnx.close()


    def executeSP(self):
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.callproc('sp_getUsers')

        print("estoy imprimiendo el metodo")
        for result in cursor.stored_results():
            print(result.fetchall())

        cnx.commit()
        cnx.close()

