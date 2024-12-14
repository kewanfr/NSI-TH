def couples_consecutifs(tab):
    """
    Entrées:
        - tab, list de int, un tableau d'entiers
    Sorties:
        - couples, liste de tuple de int, couples consécutifs de tab
    Rôle: retourne les couples consécutifs d'entiers de tab
    Préconditions:
        - tab est un tableau d'entiers
        - tab est non vide
    """

    if not isinstance(tab, list):
        print("Erreur: tab doit être une liste")
        return None

    if len(tab) == 0:
        print("Erreur: tab ne doit pas être vide")
        return None

    if not all(isinstance(x, int) for x in tab):
        print("Erreur: tous les éléments de tab doivent être des entiers")
        return None

    couples = []  # On initialise un tableau de couples non vides

    # On parcourt les éléments du tableau en s'arretant à n - 1
    # Afin d'éviter une index erreur quand on fait tab[i+1]
    # Si len(tab) == 1, la valeur sera de 0 donc la boucle
    # Ne s'exécutera pas
    for i in range(len(tab) - 1):
        # Si le nombre actuel et le suivant sont des nombres consécutifs
        if tab[i] + 1 == tab[i + 1]:
            # On ajoute le couple dans notre tableau
            couples.append((tab[i], tab[i + 1]))

    return couples  # On renvoie le tableau


if __name__ == "__main__":
    # On teste la fonction avec des exemples
    # Exemples du sujet
    print(couples_consecutifs([1, 4, 3, 5]))
    print(couples_consecutifs([1, 4, 5, 3]))
    print(couples_consecutifs([1, 1, 2, 4]))
    print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
    print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))

    # Cas critiques
    print(couples_consecutifs([1]))
    print(couples_consecutifs([]))
    print(couples_consecutifs("tab"))
    print(couples_consecutifs(["1"]))
