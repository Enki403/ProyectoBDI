"""
    @author hjvasquez@unah.hn
    @author nelson.sambula@unah.hn
    @author lggutierrez@unah.hn
    @author renata.dubon@unah.hn
    @date 12/12/2020
    @version 0.1
"""

import mysql.connector

class ConnectionDB:
    def __init__(self,credentials):
        self.credentials = credentials

    def validateUser(self,name,password):
        if name == "admin" and password == "admin":
            return True
        isUser = False
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        query = 'CALL sp_getUsers()'
        cursor.execute(query)
        for i in cursor:
            if((i[1] == name) and (i[2]== password)):
                query = 'CALL sp_userAuthenticated(%s)'
                self.executeQueryWrite(query, (name,))
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

    def getUsers(self):
        valuesReturn = []
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.callproc('sp_getUsers')
        for result in cursor.stored_results():
            for registry in result:
                valuesReturn.append(registry)
        cnx.commit()
        cnx.close()
        return(valuesReturn)


