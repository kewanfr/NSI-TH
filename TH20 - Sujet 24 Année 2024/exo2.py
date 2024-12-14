# def somme_max(tab):
#     n = len(tab)
#     sommes_max = [0] * n
#     sommes_max[0] = tab[0]
#     # On calcule la plus grande somme se terminant en i
#     for i in range(1, n):
#         if sommes_max[i - 1] + tab[i] > ...:
#             sommes_max[i] = ...
#         else:
#             sommes_max[i] = ...
#     # on en déduit la plus grande somme de celles-ci
#     for i in range(1, n):
#         if ... > ...:
#             maximum = i

#     return sommes_max[...]


def somme_max(tab):
    """
    Entrées:
    - tab, list de int, liste depuis laquelle renvoyer la somme max
    Sorties:
    - int, la plus grande somme de ses éléments consécutifs
    Rôle: A partir d'un tableau d'entiers, renvoie la plus grande somme
    possible de ses éléments consécutifs
    """
    n = len(tab)  # Définit n à la taille de la list
    sommes_max = [0] * n  # Initie un tableau de la taille de tab
    sommes_max[0] = tab[0]  # L'une somme est le premier élément de tab
    # on calcule la plus grande somme se terminant en i

    # Parcourt de 1 à n (en ne parcourant pas le premier élément)
    for i in range(1, n):
        # Si la dernière somme + l'élément actuel est plus grand
        # que l'élément suivant dans tab
        if sommes_max[i - 1] + tab[i] > tab[i]:
            # La somme à i est la somme à i-1 + le dernier élément
            sommes_max[i] = sommes_max[i - 1] + tab[i]
        else:
            # Sinon, la somme en i est uniquement l'élément i de tab
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci

    # Initialise une variable pour le maximum
    maximum = 0
    # De 1 à n, on regarde si la somme est plus grande que celle trouvée
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i  # Si oui, remplace l'indice de celle trouvée

    return sommes_max[maximum]  # Renvoie la plus grande somme trouvée


print(somme_max([1, 2, 3, 4, 5]))
print(somme_max([1, 2, -3, 4, 5]))
