def grandChiffre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return max(liste[0], grandChiffre(liste[1:]))


liste = [1, 4, 7, 2, 5, 8, 3, 9, 6]
resultat = grandChiffre(liste)
print("Le plus grand chiffre de la liste", liste, "est", resultat)
