from utility_connection import ConnectionUtil

connection = ConnectionUtil()
connession = connection.get_connection()
cursor = connection.get_cursor(connession)

connection.getAllActor() 
connection.getAllActorsByFilm("ACADEMY DINOSAUR")

connection.getAllFilm()
connection.getActorById("1")

cursor.close()
connection.close_connection(connession)