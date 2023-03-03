def puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return puissance(x*x, n/2)
    else:
        return x * puissance(x*x, (n-1)/2)

x = int(input("Entrez un nombre entier : "))
n = int(input("Entrez sa puissance : "))
resultat = puissance(x, n)
print(x, "puissance", n, "=", resultat)