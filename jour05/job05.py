def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nombre = int(input("Entrez un nombre entier : "))
resultat = fibonacci(nombre)
print("Dans la suite de Fibonacci la position", nombre, "=", resultat)
