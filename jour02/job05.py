class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche, reservoir):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def __setMarque(self):
        self.__marque = input("Quelle est la marque de votre voiture?")

    def getMarque(self):
        self.__setMarque()

    def __setModele(self):
        self.__modele = input("Quelle est le modèle de votre voiture?")

    def getModele(self):
        self.__setModele()

    def __setAnnee(self):
        self.__annee = input("De quelle année est votre véhicule?")

    def getAnnee(self):
        self.__setAnnee()

    def __setKilometrage(self):
        self.__kilometrage = input("Combien de kilométrage à votre véhicule?")

    def getKilometrage(self):
        self.__setKilometrage()

    def __setEn_Marche(self):
        self.__en_marche = input("Votre voiture est en marche?(True/False)")

    def getEn_Marche(self):
        self.__setEn_Marche()

    def demmarer(self):
        self.__verifier_plein()
        if self.__verifier_plein() > int(5):
            self.__en_marche = True
        else:
            self.__en_marche = False
            print("La voiture n'a pas assez d'essence pour démarrer")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir

    def afficherInfo(self):
        if self.__en_marche == True:
            etat_voiture = "en marche."
            print("Vous avez une voiture de marque", self.__marque, "du modèle", self.__modele, "sortie en",
                  self.__annee, "qui a roulé", self.__kilometrage, "KM, elle possède actuellement", self.__reservoir,
                  "L d'essence,elle est actuellement", etat_voiture)
        elif self.__en_marche == False:
            etat_voiture = "éteinte."
            print("Vous avez une voiture de marque", self.__marque, "du modèle", self.__modele, "sortie en",
                  self.__annee, "qui a roulé", self.__kilometrage, "KM, elle possède actuellement", self.__reservoir,
                  "L d'essence,elle est actuellement", etat_voiture)


Fiat = Voiture("Fiat", "Punto", 2004, 145000, False, 5)
Fiat.demmarer()
Fiat.afficherInfo()
Fiat.getMarque()
Fiat.getModele()
Fiat.getAnnee()
Fiat.getKilometrage()
Fiat.getEn_Marche()
Fiat.demmarer()
Fiat.afficherInfo()