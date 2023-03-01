class CompteBancaire:
    def __init__(self, numCompte, nom, prenom, solde, decouvert):
        self.__numCompte = numCompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Le compte de", self.__nom, self.__prenom, "numéro", self.__numCompte, "contient", self.__solde, "€")

    def afficherSolde(self):
        print("Votre solde est de:", self.__solde, "€")

    def versement(self, montant):
        self.__solde += montant
        print("Vous avez reçu un versement de", montant, "€", "Votre solde est désormais de", self.__solde, "€")

    def retrait(self, montant):
        if self.__decouvert == True:
            self.__solde -= montant
            print("Vous venez de retirez", montant, "€", "Votre solde est désormais de", self.__solde, "€")
            self.agios()
        elif self.__solde < montant:
            print("Votre compte ne permet pas de découvert")
        elif self.__solde >= montant:
            self.__solde -= montant
            print("Vous venez de retirez", montant, "€", "Votre solde est désormais de", self.__solde, "€")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= 10
            print("Des frais de découvert on était perçu, votre solde est désormais de", self.__solde, "€")
        elif self.__solde > 0:
            pass

    def virement(self, compte, montant):
        if self.__solde < 0:
            print("Vous êtes a découvert vous ne pouvez pas faire de virement")
        elif self.__solde < montant:
            print("Vous ne possédé pas cette somme sur votre compte")
        elif self.__solde >= montant:
            compte.versement(montant)
            self.__solde -= montant
            print("Vous venez d'effectuer un virement de", montant, "€")


compte1 = CompteBancaire(78848984, "Abdul", "Ziz", 800, False)
compte2 = CompteBancaire(667420, "Farouk", "Hermit", -300, True)

compte1.afficher()
compte1.afficherSolde()
compte1.versement(10)
compte1.retrait(110)
compte2.afficher()
compte1.virement(compte2, 300)
compte1.afficher()
compte2.afficher()
