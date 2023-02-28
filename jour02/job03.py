class Livre:
    def __init__(self, titre, auteur, nbPages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages
        self.__disponible = disponible

    def verification(self):
        if self.__disponible == True:
            return True
        if self.__disponible == False:
            return False

    def emprunter(self):
        if self.verification() == True:
                print("Le livre est disponible vous l'emprunter")
                self.__disponible=False
        else:
            print("Le livre n'est pas disponible il ne peut donc pas être emprunté")


    def rendre(self):
        if self.verification()==False:
                print("Le livre a était rendu")
                self.__disponible=True
        elif self.verification() == True:
            print("Vous n'avez aucun livre a rendre")

    def __setTitre(self):
        self.__titre = input("Quelle est le titre de votre livre?\n")
        return self.__titre

    def getTitre(self):
        self.__setTitre()

    def afficherTitre(self):
        return self.__titre

    def __setAuteur(self):
        self.__auteur = input("Quelle est le nom de l'auteur?\n")
        return self.__auteur

    def getAuteur(self):
        self.__setAuteur()

    def afficherAuteur(self):
        return self.__auteur

    def __setnbPages(self):
        self.__nbPages = input("Combien de page possède le livre?\n")
        if "." in self.__nbPages or "," in self.__nbPages:
            print("La valeur entrée est invalide veuillez entrée un nombre entier positif.\n")
            self.__setnbPages()
        elif self.__nbPages < str(0) or self.__nbPages.isalpha():
            print("La valeur entrée est invalide veuillez entrée un nombre entier positif.\n")
            self.__setnbPages()
        else:
            return self.__nbPages

    def getnbPages(self):
        self.__setnbPages()

    def affichernbPage(self):
        return self.__nbPages


dictionnaire = Livre("Larousse", "Jack", 40, True)
print("Le titre du livre est:", dictionnaire.afficherTitre())
print("L'auteur du livre est:", dictionnaire.afficherAuteur())
print("Le livre possède:", dictionnaire.affichernbPage(), "pages")
dictionnaire.emprunter()
dictionnaire.rendre()
dictionnaire.getTitre()
dictionnaire.getAuteur()
dictionnaire.getnbPages()
print("Le titre du livre est:", dictionnaire.afficherTitre())
print("L'auteur du livre est:", dictionnaire.afficherAuteur())
print("Le livre possède:", dictionnaire.affichernbPage(), "pages")
