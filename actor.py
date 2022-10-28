from utility_connection import ConnectionUtil

connection = ConnectionUtil()
connession = connection.get_connection()
cursor = connection.get_cursor(connession)

connection.getAllActor() 
connection.getAllActorsByFilm("ACADEMY DINOSAUR")

connection.getAllFilm()

cursor.close()
connection.close_connection(connession)