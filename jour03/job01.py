class Ville:
    def __init__(self, nom, habitant):
        self.__nom = nom
        self.__habitant = habitant

    def afficherPopulation(self):
        print("Populations de la ville de", self.__nom, ":", self.__habitant, "habitants.")

    def majHabitant(self, majHabitant):
        self.__habitant += majHabitant

    def afficherMajHabitant(self):
        print("Mise a jour de la population de la ville de", self.__nom, self.__habitant, "habitants")


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self, ville):
        self.__ajoutHabitant = 0
        self.__ajoutHabitant += 1
        ville.majHabitant(self.__ajoutHabitant)


ville1 = Ville("Paris", 1000000)
ville1.afficherPopulation()

ville2 = Ville("Marseille", 861635)
ville2.afficherPopulation()

personne1 = Personne("John", 45, "Paris")
personne1.ajouterPopulation(ville1)
personne2 = Personne("Myrtille", 4, "Paris")
personne2.ajouterPopulation(ville1)
personne3 = Personne("Chloé", 18, "Marseille")
personne3.ajouterPopulation(ville2)
ville1.afficherMajHabitant()
ville2.afficherMajHabitant()
