def comparer_chaines():
    chaine1 = input("Entrez la première chaîne de caractère : ")
    chaine2 = input("Entrez la deuxième chaîne de caractère : ")

    def comparer_chaines_recursive(x, y):
        if x == len(chaine1) and y == len(chaine2):
            return 1
        elif y < len(chaine2) and chaine2[y] == '*':
            while y < len(chaine2) and chaine2[y] == '*':
                y += 1
            if y == len(chaine2):
                return 1
            else:
                for z in range(x, len(chaine1) + 1):
                    if comparer_chaines_recursive(z, y):
                        return 1
                return 0
        elif x < len(chaine1) and y < len(chaine2) and chaine1[x] == chaine2[y]:
            return comparer_chaines_recursive(x+1, y+1)
        else:
            return 0

    chaine1 = chaine1.lower()
    chaine2 = chaine2.lower()
    return comparer_chaines_recursive(0, 0)

resultat = comparer_chaines()
print(resultat)

