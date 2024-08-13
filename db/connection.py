import mysql.connector
from mysql.connector import MySQLConnection

class DatabaseConnection:
    def __init__(self, host: str, user: str, passwd: str, database: str):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.connection = None

    def connect(self) -> MySQLConnection:
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
        print("Connection established")
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

