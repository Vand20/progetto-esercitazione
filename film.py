from utility_connection import MySql

class Film:

    def getAllFilm(self):
        a = MySql()
        a.execute("select * from film")
        all_film = a.fetchall()

        return all_film

    def getFilmByTitle(self, title):
        d = MySql()
        d.execute(f"select * from film where title = '{title}'")
        film_by_title = d.fetchall()
        d.close_connection()

        return film_by_title

    def getFilmByLength(self):
        a = MySql()
        a.execute("select * from film where length > 120")
        all_film_by_length = a.fetchall()

        return all_film_by_length

film = Film()

print(film.getAllFilm())
print(film.getFilmByTitle('ACE GOLDFINGER'))
print(film.getFilmByLength())