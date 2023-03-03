def longueur(chaine_de_caractere):
    if chaine_de_caractere == "":
        return 0
    else:
        return 1 + longueur(chaine_de_caractere[1:])


chaine_de_caractere = input("Entrez une chaîne de caractères : ")
resultat = longueur(chaine_de_caractere)
print("La longueur de :", chaine_de_caractere, " est de :", resultat, "caractère")
