def propager(M, i, j, val):
    """
    Entrées:
        - M list de list de 0 ou 1, image binaire de pixels
            représentée par un tableau à 2 dimensions
        - i int, indice de ligne
        - j int, indice de colonne
        - val int, la valeur à laquelle mettre les pixels
              de la composante du pixel M[i][j] qui valent 1
    Sorties: Aucune
    Rôle: Selon une image représentée par un tab à 2 dimensions,
          Modifie la list M, mets à jours tous les éléments d'une
          même composante à la valeur de val
    """
    # Cas de base: Si l'élément est égal à 1, on le mets à val
    print(len(M) - (i - j), "i - j")
    if M[i][j] == 1:
        M[i][j] = val

    # L'élément en haut fait partie de la composante
    if i - 1 >= 0 and M[i - 1][j] == 1:
        propager(M, i - 1, j, val)

    # L'élément en bas fait partie de la composante
    if i + 1 < len(M) and M[i + 1][j] == 1:
        propager(M, i + 1, j, val)

    # l'élément à gauche fait partie de la composante
    if j - 1 >= 0 and M[i][j - 1] == 1:
        propager(M, i, j - 1, val)

    # l'élément à droite fait partie de la composante
    if j + 1 < len(M[i]) and M[i][j + 1] == 1:
        propager(M, i, j + 1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
propager(M, 2, 1, 3)
print(M)
