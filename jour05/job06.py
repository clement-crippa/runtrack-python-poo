def emplacementValide(plateau, ligne, colonne):
    w = len(plateau)
    for x in range(ligne):
        if plateau[x][colonne] == 'X':
            return False
        y = ligne - x
        if colonne - y >= 0 and plateau[x][colonne - y] == 'X':
            return False
        if colonne + y < w and plateau[x][colonne + y] == 'X':
            return False
    return True


def placementReine(plateau, ligne):
    w = len(plateau)
    if ligne == w:
        return True

    for colonne in range(w):
        if emplacementValide(plateau, ligne, colonne):
            plateau[ligne][colonne] = 'X'
            if placementReine(plateau, ligne + 1):
                return True
            plateau[ligne][colonne] = 'O'

    return False


def affichagePlateau(plateau):
    for ligne in plateau:
        print(' '.join(ligne))


w = int(input("Saisir un entier (taille du tableau): "))
plateau = [['O' for x in range(w)] for y in range(w)]
placementReine(plateau, 0)
affichagePlateau(plateau)
