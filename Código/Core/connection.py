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


    # def executeSP(self):
    #     valuesReturn = []
    #     cnx = mysql.connector.connect(**self.credentials)
    #     cursor = cnx.cursor()
    #     cursor.callproc('sp_getUsers')

    #     print("estoy imprimiendo el metodo")
    #     for result in cursor.stored_results():
    #         # print(result.fetchall())
    #         for x in result.fetchall():
    #             data = [line for line in x]  
    #             for i in x:
    #                 aux = []
    #                 if isinstance(i, bytearray):
    #                     i = i.decode("utf-8")
    #                 aux.append(i)
    #             valuesReturn.append(aux)
    #         #     print(range(len(x)))
    #         #     for i in x:

    #         #         if isinstance(i,bytearray):
    #         #         if isinstance(i,bytearray):
    #         #             i = i.decode('utf-8')
    #         #             # print(otra)
    #         #             # print("de la instancia")
    #         #     #     aux.append(i)
    #         #     # valuesReturn.append(aux)
    #         #             # print(i)
    #         #             # print("este es un id")



    def executeSP(self):
        valuesReturn = []
        aux = []
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.callproc('sp_getUsers')

        for result in cursor.stored_results():
            for x in result.fetchall():
                for i in x:
                    if isinstance(i,bytearray):
                    if isinstance(i,bytearray):
                        i = i.decode('utf-8')
                    aux.append(i)
                valuesReturn.append(aux)



        print(valuesReturn)

        cnx.commit()
        cnx.close()

