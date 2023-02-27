class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        print("L'age de l'animal", self.age, "ans")
        self.age += 1
        print("L'age de l'animal", self.age, "ans")

    def nommer(self):
        print("L'animal se nomme", self.prenom)


age = 0
prenom = ""
chien = Animal(age, "Luna")
chien.vieillir()
chien.nommer()
