def ajoute(indice, element, tab):
    """
    Entrées :
        - indice, int, indice où insérer l'élément
        - element, int, élément à insérer
        - tab, list, tableau d'entiers
    Sorties :
        - list, tableau d'entiers avec l'élément inséré à l'indice donné
    Rôle: Insère un élément dans un tableau à l'indice donné
    """
    nbre_elts = len(tab)  # Nombre d'éléments dans le tableau
    tab_ins = [0] * (nbre_elts + 1)  # Tableau avec n + 1 éléments

    # On copie les éléments avant l'indice
    for i in range(indice):
        tab_ins[i] = tab[i]  # Copie de l'élément à insérer
    tab_ins[indice] = element  # Copie de l'élément à l'indice

    # On copie les éléments après l'indice
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i - 1]

    # On renvoie le tableau avec l'élément inséré
    return tab_ins


print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(0, 4, [7, 8, 9]))
