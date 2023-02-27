class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)


presentation1 = Personne("Doe", "John")
presentation2 = Personne("Dupond", "Jean")

presentation1.SePresenter()
presentation2.SePresenter()
