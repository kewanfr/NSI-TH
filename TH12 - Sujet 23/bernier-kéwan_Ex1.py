def selection_enclos(table_animaux, num_enclos):
    """
    Entrées:
        - table_animaux: tableau de dictionnaires d'animaux,
          avec les clés: 'nom', 'espece' (strs), 'age' et 'enclos' (ints)
        - num_enclos: numéro de l'enclos à sélectionner
    Sortie:
        - table_animaux_enclos: tableau de dict des enregistrements de
          table_animaux dont l'attribut 'enclos' est num_enclos
          ou None si les entrées ne sont pas bonnes
    Role: Renvoie la liste des animaux dans l'enclos num_enclos

    Exemples du sujet: 
    >>> animaux = [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},\
    {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},\
    {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},\
    {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},\
    {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
    >>> selection_enclos(animaux, 5)
    [{'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5},
    {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]
    >>> selection_enclos(animaux, 2)
    [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}]
    >>> selection_enclos(animaux, 7)
    []

    Tests des erreurs: 
    >>> selection_enclos(animaux, "7")
    Erreur: num_enclos doit être un entier
    >>> selection_enclos([], 5)
    []
    >>> selection_enclos(["chien", \
    {'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}], 5)
    Erreur: Les éléments de table_animaux doivent être des dictionnaires
    >>> selection_enclos([{'nom': 'Medor', 'espece': 'chien', 'age': 5}], 5)
    Erreur: les dictionnaires doivent contenir la clé 'enclos'
    """

    # On vérifie que num_enclos est un entier
    if not isinstance(num_enclos, int):
        # Sinon on print une erreur et renvoie None
        print("Erreur: num_enclos doit être un entier")
        return None

    # On vérifie que la table d'animaux n'est pas vide
    if len(table_animaux) < 1:
        # Sinon on renvoie une liste vide
        return []

    # On vérifie si les éléments de table_animaux sont des dictionnaires
    if not all([isinstance(animal, dict) for animal in table_animaux]):
        # Sinon on print une erreur et renvoie None
        print(
            "Erreur: Les éléments de table_animaux "
            "doivent être des dictionnaires"
        )
        return None

    # On vérifie que tous les dictionnaires contiennent la clé 'enclos'
    if not all(["enclos" in animal for animal in table_animaux]):
        # Sinon on print une erreur et renvoie None
        print("Erreur: les dictionnaires doivent contenir la clé 'enclos'")
        return None

    table_animaux_enclos = []  # On initalise une liste d'animaux vide
    for animal in table_animaux:  # On parcours la liste d'animaux
        # Si l'animal est dans l'enclos spécifié
        if animal["enclos"] == num_enclos:
            table_animaux_enclos.append(animal)  # on l'ajoute à la liste
    return table_animaux_enclos  # On renvoie la liste


if __name__ == "__main__":  # Si le fichier est lancé et non pas importé
    # On exécute la vérification de doctest dans la docstring
    import doctest

    # On ajoute NORMALIZE_WHITESPACE pour éviter les fausses erreurs
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
