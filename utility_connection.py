import mysql.connector
from mysql.connector import Error

class ConnectionUtil:

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='sakila',
                user='root',
                password='Daniele68!'
            )
            if self.connection.is_connected():
                print('Connection established')
        except Error as e:
            print(e)
        return self.connection

    def get_cursor(self, connection):
        self.cursor = connection.cursor()
        print('Cursor created')
        return self.cursor

    def close_connection(self, connection):
        connection.close()
        print('Connection closed')

    def getAllActor(self):
        self.cursor.execute(
        """
        SELECT first_name, last_name
        FROM Actor
        ORDER BY last_name
        """
        )
        records = self.cursor.fetchall()
        for row in records:
            print(row)

    def getAllActorsByFilm(self,filmTitle):
        self.cursor.execute(
            """
            SELECT f.title, count(*) 
            FROM actor a, film_actor fa, film f
            WHERE a.actor_id = fa.actor_id 
            AND fa.actor_id = f.film_id
            GROUP BY f.title
            """
        )
        records = self.cursor.fetchall()
        for row in records:
            print(row)
    
    def getAllFilm(self):
        self.cursor.execute(
            """
            SELECT * 
            FROM film
            """
        )
        film = self.cursor.fetchall()
        for x in film:
            print(x)

    def getActorById(self):
        self.cursor.execute(
            """
            SELECT actor_id
            FROM actor
            """
        )
        actor_id = self.cursor.fetchall()
        for i in actor_id:
            print(i)

    def getFilmByTitle(self):
        self.cursor.execute(
            """
            SELECT title
            FROM film
            """
        )
        film = self.cursor.fetchall()
        for i in film:
            print(i)
