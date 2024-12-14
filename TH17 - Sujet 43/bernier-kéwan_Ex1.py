def ecriture_binaire_entier_positif(n):
    """
    Entrées:
        - n, int positif, le nombre décimal à convertir en binaire

    Sorties:
        - liste_entiers, list de int (0 ou 1), liste d'entiers
        correspondant à l'écriture binaire de n
        ou None s'il y a une erreur

    Rôle: Convertit un entier décimal en nombre binaire sous forme
    d'une liste d'entiers
    """
    # On vérifie que n est un entier
    if not isinstance(n, int) or n < 0:
        # On affiche un message d'erreur
        print("Erreur: n doit être un entier positif")
        return None  # On renvoie None

    # Si n est égal à 0, on renvoit directement [0]
    if n == 0:
        return [0]

    liste_entiers = []  # On initialise la liste d'entiers

    # On calcule le reste de la division euclidienne de n par 2
    # Si c'est 0, le nombre binaire est 0 ou 1 si c'est 1
    b = n % 2

    # On définit n au résultat de la division euclidienne de n par 2
    n = n // 2  #

    # On ajoute le reste obtenir à notre liste d'neiters
    liste_entiers.append(b)

    # Tant que n n'est pas nul
    while n > 0:
        # On recalcule le résultat et le reste de la division euclidienne
        b = n % 2
        n = n // 2

        # On ajoute la valeur du reste de la division en dans la liste
        liste_entiers.append(b)  # On ajoute à la liste la

    # On renverse les éléments de la liste
    liste_entiers.reverse()

    return liste_entiers  # On renvoie la liste


print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))
print(ecriture_binaire_entier_positif(0))
