from configparser import ConfigParser
import mysql.connector

class DBConfig:
    def __init__(self):
        # Definicendo el nombre del archivo y leendolo
        fileName = 'config.ini'
        config = ConfigParser()
        config.read(fileName)

        #Creando archivo de configuracion de Mysql
        configDB = {
            'user': config['DATABASES']['user'],
            'password': config['DATABASES']['pass'],
            'host': config['DATABASES']['host'],
            'database': config['DEFAULT']['db']
        }

        self.mydb = mysql.connector.connect(**configDB)



