def recherche(elt, tab):
    """
    Entrées:
        - elt (int): nombre entier à rechercher dans tab
        - tab (list de int): tableau d'int dans lequel rechercher elt

    Sortie:
        - i, l'indice de la dernière occurence de elt dans tab
        ou None si elt n'est pas dans tab

    Rôle: Renvoie l'indice de la dernière occurence de elt dans tab
    """

    # On vérifie que elt est un entier
    if not isinstance(elt, int):
        print("Erreur: elt doit être un entier")
        return None

    # On vérifie que tab est une liste
    if not isinstance(tab, list):
        print("Erreur: tab doit être une liste")
        return None

    # On vérifie que tab est une liste d'entiers
    if not all(isinstance(i, int) for i in tab):
        print("Erreur: tab doit être une liste d'entiers")
        return None

    # Si tab est vide, on renvoie None
    if len(tab) == 0:
        return None

    result = None  # On initialise le résultat à None

    # On parcourt le tableau tab
    for i in range(len(tab)):
        # Si on trouve elt, on met à jour le résultat
        if tab[i] == elt:
            result = i

    # On renvoie l'indice de la dernière occurence de elt dans tab
    return result
