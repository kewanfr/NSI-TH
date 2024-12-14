# def parcours_largeur(arbre, liste_etiquettes=[]):
#     liste_etiquettes = liste_etiquettes
#     if arbre == None:
#         return liste_etiquettes
#     elif isinstance(arbre, tuple):
#         liste_etiquettes.append(parcours_largeur(arbre, liste_etiquettes))
#     else:
#         liste_etiquettes.append(parcours_largeur(arbre[0], liste_etiquettes))
#         liste_etiquettes.append(parcours_largeur(arbre[1], liste_etiquettes))
#         liste_etiquettes.append(parcours_largeur(arbre[2], liste_etiquettes))


def parcours_largeur(arbre):
    """
    Entrées:
    - arbre, tuple de 1 tuple, 1 valeur et un autre tuple,
        ce qui représente notre arbre
    Sorties: - list de any, liste de toutes les valeurs de l'arbre
    Rôle: Effectue et renvoie le parcours en largeur sur un arbre
    """

    if not isinstance(arbre, tuple):
        print("Erreur: arbre doit être un 3-uplet")
        return None

    tuples = [arbre]  # On met l'arbre dans une liste des tuples
    etiquettes = []  # Initialise la liste des

    # Parcourt la liste tuples
    while len(tuples) != 0:
        # Retire
        x = tuples.pop(0)
        etiquettes.append(x[1])
        if x[0] != None:
            tuples.append(x[0])
        if x[2] != None:
            tuples.append(x[2])
    return etiquettes


arbre = (
    ((None, 1, None), 2, (None, 3, None)),
    4,
    ((None, 5, None), 6, (None, 7, None)),
)
print(parcours_largeur(arbre))
arbre2 = [
    ((None, 1, None), 2, (None, 3, None)),
    4,
    ((None, 5, None), 6, (None, 7, None)),
]
print(parcours_largeur(arbre2))
