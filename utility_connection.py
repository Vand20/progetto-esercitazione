import mysql.connector
from mysql.connector import Error

class MySql:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', database='sakila', user='root', password='Daniele68!')
            self.cursor = self.conn.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def close_connection(self):
        if (self.conn is not None):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")

    def execute(self, sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()