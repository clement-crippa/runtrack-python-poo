class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def __setLongueur(self):
        self.__longueur = input("Quelle longueur désirez-vous?\n")
        return self.__longueur

    def getLongueur(self):
        self.__setLongueur()

# Mutateur
    def __setLargeur(self):
        self.__largeur = input("Quelle largeur désirez-vous?\n")
        return self.__largeur
# Accesseur
    def getLargeur(self):
        self.__setLargeur()

    def afficherLongueur(self):
        return self.__longueur

    def afficherLargeur(self):
        return self.__largeur


rectangle = Rectangle(10, 5)
print("La longueur est de:", rectangle.afficherLongueur())
print("La largeur est de:", rectangle.afficherLargeur())
rectangle.getLongueur()
rectangle.getLargeur()
print("La longueur est de:", rectangle.afficherLongueur())
print("La largeur est de:", rectangle.afficherLargeur())
