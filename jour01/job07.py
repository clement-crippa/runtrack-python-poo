class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def position(self):
        coordonnees = (self.x, self.y)
        return coordonnees


deplacement = Personnage(5, 5)
print(deplacement.position())
deplacement.gauche()
print(deplacement.position())
deplacement.bas()
print(deplacement.position())
deplacement.droite()
print(deplacement.position())
deplacement.haut()
print(deplacement.position())
