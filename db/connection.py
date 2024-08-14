import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, passwd, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.connection = None

    def connect(self):
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


