class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        print("Voici un cercle de rayon", rayon)

    def changerRayon(self, rayon):
        self.rayon = rayon
        print("Le rayon est désormais de", rayon)

    def circonference(self):
        circonference_total = (3.14 * 2 * self.rayon)
        return circonference_total

    def aire(self):
        aire_total = (3.14 * (self.rayon ** 2))
        return aire_total

    def diametre(self):
        diametre_total = (self.rayon * 2)
        return diametre_total

    def afficherInfos(self):
        print("La circonférence est de:", dessin.circonference(), "cm")
        print("L'aire est de:", dessin.aire(), "cm")
        print("Le diamètre du cercle est de:", dessin.diametre(), "cm")


dessin = Cercle(4)
print("La circonférence est de:", dessin.circonference(), "cm")
print("L'aire est de:", dessin.aire(), "cm")
print("Le diamètre du cercle est de:", dessin.diametre(), "cm\n")
dessin.changerRayon(7)
dessin.afficherInfos()
