tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]

tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]

tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]


def trouver_intrus(tab, g, d):
    """
    Entrées:
        - tab, list de int, le tableau dans lequel chercher l'intrus
        - g, int, l'indice de gauche de la recherche (début)
        - d, int, l'indice de droite de la recherche (fin)
    Sortie:
        - int, la valeur de l'intrus ou None si elle n'existe pas
    Rôle: Renvoie la valeur de l'intrus situe entre les indices g et d
    dans la liste tab ou :
        tab verifie les conditions de l'exercice,
        g et d sont des multiples de 3.
    """
    # On vérifie le cas de base:
    # les deux indices de recherche sont les mêmes
    if g == d:
        return tab[g]

    else:
        # Sinon, on prends le milieu du nombre de triplets
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        # Si le nombre et celui de droite sont égaux, on passe à droite
        if tab[indice] == tab[indice + 1]:
            return trouver_intrus(tab, indice + 3, d)
        else:
            # Sinon, on prends la partie gauche
            return trouver_intrus(tab, g, indice)


print(
    trouver_intrus(
        [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5],
        0,
        21,
    )
)

print(trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3], 0, 12))

print(trouver_intrus([5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8], 0, 15))
