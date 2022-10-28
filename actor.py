from utility_connection import MySql

class Actor:

    def getAllActors(self):
        a = MySql()
        a.execute("select * from actor order by last_name ")
        all_actors = a.fetchall()
        a.close_connection()

        return all_actors

    def getAllActorsByFilm(self, filmTitle):
        b = MySql()
        b.execute(f"select a.first_name, a.last_name from actor a, film_actor fa, film f where a.actor_id = fa.actor_id and fa.film_id = f.film_id and f.title = '{filmTitle}'")
        all_actors_by_film = b.fetchall()
        b.close_connection()

        return all_actors_by_film

    def getActorById(self, id):
        c = MySql()
        c.execute(f"select first_name, last_name from actor where actor_id = '{id}'")
        actor_by_id = c.fetchall()
        c.close_connection()

        return actor_by_id

    def getBestActorsName(self):
        d = MySql()
        d.execute(f"select count(fa.film_id) as num_film, a.first_name, a.last_name from actor a, film_actor fa where a.actor_id = fa.actor_id having num_film > 15")
        best_actors = d.fetchall()
        d.close_connection()

        return best_actors


actors = Actor()

print(actors.getAllActors())
print(actors.getAllActorsByFilm('ACADEMY DINOSAUR'))
print(actors.getActorById('1'))