class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self, modele):
        print("Marque =", self.marque)
        print("Modèle =", modele)
        print("Année =", self.annee)
        print("Prix =", self.prix)

    def demarrer(self):
        print("Attention,je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        self.portes = 4
        self.modele = modele
        Vehicule.__init__(self, marque, annee, prix)

    def demarrer(self):
        Vehicule.demarrer(self)
        print("Vroom")


    def informationsVehicule(self):
        Vehicule.informationsVehicule(self, self.modele)
        print("Nombre de porte=", self.portes)


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        self.roue = 2
        self.modele = modele
        Vehicule.__init__(self, marque, annee, prix)

    def demarrer(self):
        Vehicule.demarrer(self)
        print("2 roue sur la piste")

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self, self.modele)
        print("Nombre de roue=", self.roue)


voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()
print("---------------")
voiture.demarrer()
print("-----------------------")
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
print("---------------")
moto.demarrer()
