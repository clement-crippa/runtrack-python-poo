class Personne:
    def __init__(self, age):
        self.age = age

    def afficherAge(self):
        print("Age:", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self):
        self.age = input("Quelle est votre age?")
        if "." in self.age:
            print("Votre age doit être un nombre entier")
            self.modifierAge()
        elif self.age.isalpha():
            print("Votre age doit être un nombre entier")
        else:
            return self.age


class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self, 14)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")


class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencé")


personne = Personne("")
eleve = Eleve()

eleve.afficherAge()
