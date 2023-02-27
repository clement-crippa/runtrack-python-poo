class Produits:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT + (self.TVA * self.prixHT)
        return prixTTC

    def modificationNom(self, nom):
        self.nom = nom

    def modificationprixHT(self, prixHT):
        self.prixHT = prixHT

    def afficherNom(self):
        return self.nom

    def afficherprixHT(self):
        return self.prixHT

    def afficherTVA(self):
        return self.TVA

    def afficherprixTTC(self):
        return self.CalculerPrixTTC()

    def afficher(self):
        produits = (
            "Produit:", self.nom, "Prix TTC:", self.CalculerPrixTTC(), "€", "TVA:", self.TVA, "Prix HT", self.prixHT,
            "€")
        return produits


chien = Produits("Bulldog", 6550, 0.20)
print(chien.afficher())
chien.modificationNom("Chien")
chien.modificationprixHT(6)
print("\nProduits:", chien.afficherNom())
print("Prix HT:", chien.afficherprixHT(), "€")
print("TVA", chien.afficherTVA())
print("Prix TTC:", chien.afficherprixTTC(), "€\n")

piano = Produits("Piano en acajou", 999, 0.20)
print("Produits:", piano.afficherNom())
print("Prix HT:", piano.afficherprixHT(), "€")
print("TVA", piano.afficherTVA())
print("Prix TTC:", piano.afficherprixTTC(), "€\n")

voiture = Produits("Audi", 80540, 0.20)
print(voiture.afficher())
