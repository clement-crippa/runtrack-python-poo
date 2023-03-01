class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes = 0
        self.jaunes = 0
        self.rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    def recevoirUnCartonRouge(self):
        self.rouges += 1

    def afficherStatistiques(self):
        print("Statistiques de:", self.nom)
        print("Buts:", self.buts)
        print("Passes décisives:", self.passes)
        print("Cartons jaunes:", self.jaunes)
        print("Cartons rouges:", self.rouges)


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.listeJoueurs = []

    def ajouterJoueur(self, joueur):
        self.listeJoueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print("Statistiques de l'équipe", self.nom)
        for joueur in self.listeJoueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, statistique):
        if statistique == "but":
            joueur.buts += 1
        elif statistique == "passe":
            joueur.passes += 1
        elif statistique == "jaune":
            joueur.jaunes += 1
        elif statistique == "rouge":
            joueur.rouges += 1


joueur1 = Joueur("Aziz", 10, "attaquant")
joueur2 = Joueur("Farouk", 7, "attaquant")
joueur3 = Joueur("Ziz", 2, "attaquant")
joueur4 = Joueur("Abdul", 8, "attaquant")

equipe1 = Equipe("Bleu")
equipe2 = Equipe("Rouge")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur1, "passe")
equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur1, "passe")
equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur1, "jaune")
equipe1.mettreAJourStatistiquesJoueur(joueur2, "passe")
equipe1.mettreAJourStatistiquesJoueur(joueur2, "passe")
equipe2.mettreAJourStatistiquesJoueur(joueur3, "jaune")
equipe2.mettreAJourStatistiquesJoueur(joueur3, "rouge")
equipe2.mettreAJourStatistiquesJoueur(joueur3, "jaune")
equipe2.mettreAJourStatistiquesJoueur(joueur3, "rouge")
equipe2.mettreAJourStatistiquesJoueur(joueur4, "jaune")
equipe2.mettreAJourStatistiquesJoueur(joueur4, "rouge")
equipe2.mettreAJourStatistiquesJoueur(joueur4, "jaune")
equipe2.mettreAJourStatistiquesJoueur(joueur3, "rouge")

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
