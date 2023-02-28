class Student:
    def __init__(self, nom, prenom, numeroEtudiant, nombreCredits, level):
        self.__nom = nom
        self.__prenom = prenom
        self.__numeroEtudiant = numeroEtudiant
        self.__nombreCredits = nombreCredits
        self.__level = self.__studentEval()

    def __add_credits(self):
        print("L'étudiant possède actuellement", self.__nombreCredits, "points")
        creditsSupplementaire = int(input("Combien de crédit voulez vous ajouter à l'étudiant?\n"))
        if creditsSupplementaire < int(1):
            print("Vous ne pouvez pas ajouter 0 points")
            self.__add_credits()
        else:
            self.__nombreCredits = self.__nombreCredits + creditsSupplementaire
            return self.__nombreCredits

    def setcredits(self):
        self.__add_credits()

    def affichercredits(self):
        print("Le nombre de crédit de", self.__nom, self.__prenom, "est de", self.__nombreCredits, "points")

    def __studentEval(self):
        if self.__nombreCredits >= int(90):
            self.__level = "Excellent"
        elif self.__nombreCredits >= int(80):
            self.__level = "Très Bien"
        elif self.__nombreCredits >= int(70):
            self.__level = "Bien"
        elif self.__nombreCredits >= int(60):
            self.__level = "Passable"
        else:
            self.__level = "insuffisant"

    def test(self):
        self.__studentEval()

    def studenInfo(self):
        print("Nom =", self.__nom)
        print("Prénom =", self.__prenom)
        print("id =", self.__numeroEtudiant)
        print("Niveau =", self.__level)


etudiant = Student("John", "Doe", 145, 1, "")
etudiant.setcredits()
etudiant.setcredits()
etudiant.setcredits()
etudiant.test()
etudiant.affichercredits()
etudiant.studenInfo()
