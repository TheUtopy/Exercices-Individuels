# Etape 1

# Écrire une fonction sum1 qui prend un tableau d’entiers à additionner entre eux.

tab = [1, 4, 6, 8, 751, 2]

def sum1(tableau):
    sum = 0
    for number in tableau:
        sum += number

    return sum


print(sum1(tab))


# Etape 2

# Même exercice, mais avec une fonction récursive. On appellera la fonction sum2.

def sum2(tableau, result=0):
    if not tableau:
        return result
    result += tableau[0]
    # print(result)
    return sum2(tableau[1:], result)


print(sum2(tab))

# Etape 3

# On appelle factoriel le produit des entiers inférieurs ou égaux à un nombre donné. Exemple : factoriel de 3 = 1x2x3 = 6

# Écrire une fonction factorial qui prend un entier en paramètre et calcule son factoriel récursivement.

def factorial(number, result=0):
    if number == 0:
        return result
    result += number
    return factorial(number-1, result)

print(factorial(10))


# Étape 4

# Suite de Fibonacci

def fibo(x, tab=[0, 1]):
    if x == 0:
        return tab

    if tab == [0, 1]:
        x -= 2

    tab.append(tab[-1] + tab[-2])
    return fibo(x-1, tab)

print(fibo(20))

