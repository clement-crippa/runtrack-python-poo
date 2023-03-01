class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut


class ListeDeTache:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, taches):
        self.taches += [taches.titre, taches.description, taches.statut]

    def supprimerTache(self, taches):
        for i in self.taches:
            if i == taches.titre:
                position = self.taches.index(i)
                self.taches.pop(position)
                self.taches.pop(position)
                self.taches.pop(position)

    def marquerCommeFinie(self, taches):
        for i in self.taches:
            if i == taches.titre:
                position = self.taches.index(i)
                if self.taches[position + 2] == "en cours":
                    self.taches.pop(position + 2)
                    self.taches.insert(position + 2, "terminer")
                    taches.statut="terminer"

    def afficherListe(self):
        print(self.taches)

    def filterListe(self, taches):
        filtre = []
        for i in range(len(self.taches)):
            if self.taches[i] == taches.statut:
                filtre.append(self.taches[i - 2])
                filtre.append(self.taches[i - 1])
                filtre.append(self.taches[i])
        print("Liste filtré:\n", filtre)


tache1 = Tache("Ménage", "Faire le menage", "en cours")
tache2 = Tache("Cuisine", "Faire un cassoulet", "en cours")
tache3 = Tache("Poste", "Aller a la poste", "en cours")
tache4 = Tache("Chien", "Promener le chien", "en cours")
tache5 = Tache("Course", "Aller faire les course", "en cours")
tache6 = Tache("Manger", "Ne pas oublier de manger", "en cours")

liste1 = ListeDeTache()
liste1.ajouterTache(tache1)
liste1.ajouterTache(tache2)
liste1.ajouterTache(tache3)
liste1.ajouterTache(tache4)
liste1.ajouterTache(tache5)
liste1.ajouterTache(tache6)
liste1.marquerCommeFinie(tache3)
liste1.marquerCommeFinie(tache4)
liste1.afficherListe()
liste1.supprimerTache(tache1)
liste1.afficherListe()
liste1.filterListe(tache2) # Filtre les taches en cours
liste1.filterListe(tache4) # Filtre les taches terminer
