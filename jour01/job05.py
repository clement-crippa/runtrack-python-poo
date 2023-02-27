class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(self.x, self.y)

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, x):
        self.x = x
        print(self.x)

    def changerY(self, y):
        self.y = y
        print(self.y)


coordonnees = Point(10, 20)
coordonnees.afficherLesPoints()
coordonnees.afficherX()
coordonnees.afficherY()
coordonnees.changerX(4)
coordonnees.changerY(8)
