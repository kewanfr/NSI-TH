def tri_bulles(T):
    """
    Entrées:
        - T, list de int, liste d'entiers non triés à trier
    Sorties:
        - T, list de int, liste d'entiers triés par ordre croissant
    Rôle: Trier une liste d'entiers par ordre croissant en utilisant
          le tri bulle. Cela consiste à comparer les éléments 2 par 2 et
          les trier par ordre croissant, en répétant l'opération
          autant de fois que nécessaire.
    """
    n = len(T)  # On récupère la taille du tableau

    # i va de n-1 à 0, en décrémentant
    for i in range(n - 1, 0, -1):
        # On itère i fois
        for j in range(i):
            # Si elt de gauche (j) est supérieur à celui de droite (j+1)
            if T[j] > T[j + 1]:
                # On inverse les deux

                temp = T[j]  # On met l'elt j dans une variable
                T[j] = T[j + 1]  # On définit l'elt j à la val de j+1
                T[j + 1] = temp  # On définit l'elt j+1 à la valeur de j

    return T  # On renvoie le tableau trié


print(tri_bulles([]))
print(tri_bulles([7]))
print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))
print(tri_bulles([9, 7, 4, 3]))
