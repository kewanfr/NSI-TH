def tri_selection(tab):
    """
    Entrées:
        - tab, list de int, notre tableau d'entiers à trier
    Sorties:
        - tab, list de int, notre tableau d'entiers trié
          ou None s'il y a une erreur
    Rôle: Tri par ordre croissant une liste d'entiers en utilisant
          le tri sélection.
          On définit la première partie du tableau comme étant triée
          et inférieure aux éléments de la partie triée
          On prends le plus petit élément de la partie non triée
          Et on le mets à la fin de la partie triée.
    """
    # On vérifie que tab est une liste d'entiers
    if not isinstance(tab, list) or not all(isinstance(i, int) for i in tab):
        # Sinon on affiche une erreur et on renvoie None
        print("Erreur: tab doit être une liste d'entiers")
        return None

    # Si tab est vide, ou de taille 1, il est déjà trié
    if len(tab) <= 1:
        # On renvoie directement le tableau
        return tab

    n = len(tab)  # On récupère la taille de tab

    for i in range(n):  # On itère sur chaque élément de tab

        i_min = i  # On définit l'indice du plus petit élément

        for j in range(i + 1, n):
            # On itère sur le tableau pour trouver le plus petit élément

            # si l'élément trouvé est plus petit que i_min
            if tab[j] < tab[i_min]:
                # On redéfinit i_min à l'élement d'indice i
                i_min = j

        # On inverse l'élément d'indice i et le plus petit
        # Ainsi, tous les éléments avant l'indice i sont triés
        tab[i], tab[i_min] = tab[i_min], tab[i]

    return tab  # On renvoie le tableau trié


print(tri_selection([1, 52, 6, -9, 12]))
print(tri_selection([]))
print(tri_selection("5"))
print(tri_selection(["5"]))
