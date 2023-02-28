class Livre:
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages

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


dictionnaire = Livre("Larousse", "Jack", 40)
print("Le titre du livre est:",dictionnaire.afficherTitre())
print("L'auteur du livre est:",dictionnaire.afficherAuteur())
print("Le livre possède:",dictionnaire.affichernbPage(),"pages")
dictionnaire.getTitre()
dictionnaire.getAuteur()
dictionnaire.getnbPages()
print("Le titre du livre est:",dictionnaire.afficherTitre())
print("L'auteur du livre est:",dictionnaire.afficherAuteur())
print("Le livre possède:",dictionnaire.affichernbPage(),"pages")
