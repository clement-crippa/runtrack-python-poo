class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        perimetreTotal = (self.longueur + self.largeur) * 2
        print("Le périmètre totale est de:", perimetreTotal, "cm")

    def surface(self):
        surfacetotal = (self.longueur * self.largeur)
        print("La surface totale est de:", surfacetotal, "cm")

    def __setLongueur(self):
        self.longueur = int(input("Quelle est votre longueur en cm?"))
        return self.longueur

    def getLongueur(self):
        self.__setLongueur()

    def __setLargeur(self):
        self.largeur = int(input("Quelle est votre largeur en cm?"))
        return self.largeur

    def getLargeur(self):
        self.__setLargeur()

    def afficher(self):
        print("La longueur est de", self.longueur, "cm et la largeur de", self.largeur, "cm")


class Parallelepipede(Rectangle):
    def __init__(self, hauteur):
        self.hauteur = hauteur
        Rectangle.__init__(self, "", "")

    def volume(self):
        volumeTotal = self.longueur * self.largeur * self.hauteur
        print("Le volume total est de", volumeTotal, "cm")


rectangle = Rectangle(10, 20)
rectangle.afficher()
print("-----------------------")
rectangle.getLongueur()
rectangle.getLargeur()
rectangle.afficher()
rectangle.surface()
rectangle.perimetre()
print("------------------------")
paralepipede = Parallelepipede(10)
paralepipede.getLongueur()
paralepipede.getLargeur()
paralepipede.volume()
