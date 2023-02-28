class Commande:
    def __init__(self, nbCommande):
        self.__nbCommande = nbCommande
        self.__platsCommande = {}
        self.__etat = "en cours"
        self.__totalHT = 0
        self.__totalTTC = 0
        self.__tauxTVA = 20

    def ajouterPlat(self, nom_plat, prix):
        if self.__etat == "en cours":
            self.__platsCommande[nom_plat] = {"prix": prix, "etat": self.__etat}
        elif self.__etat == "annulée":
            self.__platsCommande[nom_plat] = {"prix": prix, "etat": self.__etat}
        elif self.__etat == "terminer":
            self.__platsCommande[nom_plat] = {"prix": prix, "etat": self.__etat}

    def commandeAnnulee(self):
        self.__etat = "annulée"
        print("\nLa commande a était annulée")

    def commandeTerminer(self):
        self.__etat = "terminer"
        print("\nLa commande est terminée")

    def __calculerTotal(self):
        self.__total_HT = sum([plat["prix"] for plat in self.__platsCommande.values()])
        self.__total_TTC = round(self.__total_HT * (1 + self.__tauxTVA / 100), 2)

    def commandeAfficher(self):
        self.__calculerTotal()
        tva = round(self.__total_HT * self.__tauxTVA / 100, 2)
        print(f"Numéro de commande : {self.__nbCommande}")
        for nomPlat, detailsPlat in self.__platsCommande.items():
            print(f"{nomPlat} : {detailsPlat['prix']} € ({detailsPlat['etat']})")
        print(f"Total HT : {self.__total_HT} €")
        print(f"TVA (20%) : {tva} €")
        print(f"Total TTC : {self.__total_TTC} €")

    def calculerTVA(self):
        self.__calculerTotal()
        # Arrondie la TVA à 2 décimales
        return round(self.__totalHT * self.__tauxTVA / 100, 2)


commande1 = Commande("667")
commande1.ajouterPlat("Pizza", 12.20)
commande1.ajouterPlat("Vin", 6.0)
commande1.commandeAfficher()

commande2 = Commande("668")
commande2.commandeAnnulee()
commande2.ajouterPlat("Pizza", 12.20)
commande2.ajouterPlat("Spiritueux", 12.20)
commande2.commandeAfficher()

commande3 = Commande("669")
commande3.commandeTerminer()
commande3.ajouterPlat("Pizza", 12.20)
commande3.ajouterPlat("Vin", 6.0)
commande3.ajouterPlat("Cola", 3.0)
commande3.commandeAfficher()
