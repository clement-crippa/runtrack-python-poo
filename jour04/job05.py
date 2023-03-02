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
        return airetotal


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        Forme.__init__(self)

    def aire(self):
        airetotal = (self.radius ** 2) * 3.14
        return airetotal


rectangle = Rectangle(10, 20)
print("L'aire du rectangle est de",rectangle.aire(),"cm")
cercle = Cercle(10)
print("L'aire du cercle est de",cercle.aire(),"cm")
