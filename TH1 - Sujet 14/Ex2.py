def insere(a, tab):
    """
    Entrées: 
        - a un nombre entier
        - tab un tableau d'entiers trié par ordre croissant
    Sortie: Un tableau d'entiers trié par ordre croissant contenant a
    Rôle: Insère l'élément a (int) dans le tableau tab (list) trié par ordre croissant à sa place et renvoie le nouveau tableau.
    Précondition: a doit être un nombre entier, tab doit être un tableau d'entiers trié par ordre croissant
    Postcondition: la sortie est un tableau d'entiers trié par ordre croissant contenant a
    """

    l = list(tab)
    l.append(a)
    i = len(tab) - 1 # On commence à la fin du tableau
    while a < l[i] and i >= 0: # Tant que a est plus petit que l'élément, on inverse a et l'élément d'indice i, car ça veut dire que le tableau n'est pas trié
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l

print(insere(3, [1, 2, 4, 5]))
print(insere(30, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))
print( insere(1, []))
