def recherche(caractere, chaine):
    """
    Entrées:
        - caractere, str, un caractère
        - chaine, str, une chaîne de caractères
    Sorties:
        - nb_car, int, le nombre d'occurences de caractere dans chaine
          ou None s'il y a une erreur
    Rôle: Pour un caractère et une chaîne de caractères, renvoie
    le nombre d'occurences du caractère dans la chaîne de caractères
    """
    # On vérifie que caractere est un bien une chaine de caractères
    if not isinstance(caractere, str):
        # On affiche une erreur et on renvoie None
        print("Erreur: caractere doit être de type str")
        return None

    # On vérifie que chaine est un bien une chaine de caractères
    if not isinstance(chaine, str):
        # On affiche une erreur et on renvoie None
        print("Erreur: chaine doit être de type str")
        return None

    # On vérifie que caractère est bien de longueur 1
    if not len(caractere) == 1:
        # On affiche une erreur et on renvoie None
        print("Erreur: caractère doit être de taille 1")
        return None

    if len(chaine) == 0:
        return 0  # Si la chaîne est vide, le nombre d'occurences est 0

    # On initialise un compteur à 0
    nb_occurences = 0

    # On parcourt les caractères de chaine
    for car in chaine:
        # Si le caractère est le caractère qu'on cherche
        if car == caractere:
            # On incrémente le compteur
            nb_occurences += 1

    return nb_occurences  # On renvoie le résultat du compteur


print(recherche("e", "sciences"))
print(recherche("i", "mississippi"))
print(recherche("a", "mississippi"))

# Erreurs
print(recherche(3, "sciences"))
print(recherche("e", 5))
print(recherche("ee", "sciences"))
print(recherche("f", ""))
