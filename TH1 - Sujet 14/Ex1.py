def recherche(elt, tab):
    """    
    Entrées:
        - elt un nombre
        - tab un tableau
    Sorties: Indice de elt dans tab
    Rôle: Renvoie l'indice de la première occurence de elt dans tab, ou -1 si elt n'est pas dans tab
    Précondition: elt doit être un nombre entier, tab doit contenir des nombres entiers
    Postcondition: la sortie est un entier présent dans le tableau, ou -1 sinon
    """
    assert type(elt) == int, "elt doit être un nombre entier"
    assert all(type(i) == int for i in tab), "tab doit contenir uniquement des nombres entiers"

    for i in range(len(tab)):
        if(elt == tab[i]): # Si on trouve l'élément, on renvoie son indice
            return i
    return -1

print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
print(recherche(50, []))
print(recherche(4, [2, 4, 4, 3, 4]))