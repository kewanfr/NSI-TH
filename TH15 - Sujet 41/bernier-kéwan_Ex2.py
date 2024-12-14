valeurs = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(a_rendre, rang):
    """
    Entrées:
        - a_rendre, int, la somme à rendre
        - rang, int, indice dans valeurs à partir duquel
          effectuer le rendu de monnaie
    Sorties:
        - list de int, liste des valeurs de pièces et billets à rendre
    Rôle: Renvoie la liste des valeurs de monnaie à rendre selon
          une liste de valeurs disponibles à partir de l'indice rang
          et une somme de monnaie à rendre
    """
    # Cas de base: la somme à rendre est 0
    if a_rendre == 0:
        return []

    v = valeurs[rang]
    if v <= a_rendre:
        return [v] + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang + 1)


print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291, 1))
