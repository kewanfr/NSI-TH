from random import randint


def plus_ou_moins():
    """
    Entrées: Aucune
        - Entrées de l'utilisateur
    Sorties: Aucune
    Rôle: Génère un nombre aléatoire entre 1 et 99 et demande
          à l'utilisateur de le trouver en 10 essais maximum
          En lui indiquant à chaque essai si le nombre
          est trop grand ou trop petit
    """
    nb_mystere = randint(1, 99)  # On choisit un nombre aléatoire
    # On demande à l'utilisateur de rentrer un nombre
    # Il peut y avoir une erreur s'il rentre autre chose qu'un int
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    # Si l'utilisateur ne rentre pas le bon nombre
    # Et qu'il lui reste des essais
    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        # Si l'utilisateur a gagné
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        # Si l'utilisateur a perdu
        print("Perdu ! Le nombre était ", nb_mystere)


plus_ou_moins()
