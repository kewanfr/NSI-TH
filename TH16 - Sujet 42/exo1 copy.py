def get_smaller(tab, min, max):
    smaller_i = min
    for i in range(min, max):
        element = tab[i]
        if element < tab[smaller_i]:
            smaller_i = i
    return smaller_i

    """
    Entrées:
        - tab, list de int, notre tableau d'entiers à trier
    Sorties:
        - tab, list de int, notre tableau d'entiers trié
    Rôle: Tri par ordre croissant une liste d'entiers en utilisant
          le tri sélection
    Pré-condition:
        -
    Post-condition:
        -
    """


def tri_selection(tab):
    n = len(tab)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_i]:
                min_i = j
        tab[i], tab[min_i] = tab[min_i], tab[i]
    return tab


def tri_selection(tab):

    if not isinstance(tab, list) or not all(isinstance(i, int) for i in tab):
        print("Erreur: le type de tab n'est pas bon")
        return None

    if len(tab) == 0:
        return tab

    n = len(tab)  # On récupère la taille de tab
    for i in range(n):  # On itère sur chaque élément de tab
        i_min = i  # On définit l'indice du plus petit élément

        # On itère sur le tableau pour trouver le plus petit élément
        for j in range(i + 1, n):
            if tab[j] < tab[i_min]:
                i_min = j

        # On inverse l'élément d'indice i et le plus petit
        # Ainsi, tous les éléments avant l'indice i sont triés
        tab[i], tab[i_min] = tab[i_min], tab[i]

    return tab  # On renvoie le tableau trié

    if len(tab) == 0:
        return None

    # On initialise l'indice du début (tout ce qui est avant est trié)
    # Par défaut, rien n'est encore trié
    i_debut = 0

    # On initialise l'indice de fin de tab (+1 pour que )
    i_fin = len(tab) - 1
    while i_debut != i_fin:
        i_min = i_debut
        for i in range(i_debut, i_fin):
            element = tab[i]
            if element < tab[i_min]:
                i_min = i

        tab[i_debut], tab[i_min] = (
            tab[i_min],
            tab[i_debut],
        )

        i_debut += 1
        i_min = i_debut
    return tab


print(tri_selection([1, 52, 6, -9, 12]))
print(tri_selection([]))
