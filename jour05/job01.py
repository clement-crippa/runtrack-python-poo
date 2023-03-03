def factorielle(x):
    if x < 0:
        return "Impossible de calculer un nombre négatif"
    elif x == 0:
        return 1
    else:
        return x * factorielle(x - 1)


nombre = int(input("Entrez un nombre entier : "))
resultat = factorielle(nombre)
print("La factorielle de", nombre, ":", resultat)
