from actor import Actor

class BusinessFactory:

    def getBestActors(self):

        lista_attori = Actor().getBestActorsName()
        lista_nomi = []
        lista_indici = []

        for actor in lista_attori:
            lista_nomi.append(actor[1])

        for nome in lista_nomi:
            lista_indici.append(lista_nomi.count(nome))

        for i in range(len(lista_indici)):
            if lista_indici[i] == max(lista_indici):
                return lista_nomi[i]

best_actors = BusinessFactory()

print(best_actors.getBestActors())