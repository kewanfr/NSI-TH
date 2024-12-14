def correspond(mot, mot_a_trous):
    """
    Entrées:
        - mot, str, mot à vérifier
        - mot_a_trous, str, mot à trous
    Sortie:
        - Booléen, True si on peut obtenir mot en remplaçant
        convenablement les caractères '*' de mot_a_trous
        False sinon
        ou None si il y a une erreur
    Rôle: Renvoie True si mot_a_trous correspond à mot en remplaçant
          correctement les caractères '*'
    """
    # Si mot ou mot_a_trous ne sont pas des chaines de caractères
    if not isinstance(mot, str) or not isinstance(mot_a_trous, str):
        # On affiche une erreur
        print("Erreur: mot et mot_a_trous doivent être des str")
        # Et on renvoie None
        return None

    # Si mot et mot_a_trous ne font pas la même taille
    if len(mot) != len(mot_a_trous):
        # Ils ne peuvent pas correspondre, on renvoie False
        return False

    # On initialise une variable mot_correspond à True
    # par défaut, les mots correspondent
    mot_correspond = True
    # On itère sur tous les caractères du mot
    for i, character in enumerate(mot):
        # Si le caractères n'est pas le même que celui à la mm position
        # dans mot à trous
        # ET que celui du mot à trous n'est pas une étoile
        if mot_a_trous[i] != "*" and character != mot_a_trous[i]:
            # Le mot ne correspond pas
            mot_correspond = False

    return mot_correspond


print(correspond("INFORMATIQUE", "INFO*MA*IQUE"))

print(correspond("AUTOMATIQUE", "INFO*MA*IQUE"))
print(correspond("STOP", "S*"))
print(correspond("AUTO", "*UT*"))
