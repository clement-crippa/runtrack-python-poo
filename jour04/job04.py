class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        self.longueur = longueur
        self.largeur = largeur
        Forme.__init__(self)

    def aire(self):
        airetotal = (self.longueur + self.largeur) * 2
        print("L'aire du rectangle est de:", airetotal, "cm")


forme = Forme()
print(forme.aire())
print("-----------------")
rectangle = Rectangle(10, 5)
rectangle.aire()
