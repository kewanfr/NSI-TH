def est_cyclique(plan):
    """
    Entrées:
        - plan, dict de str (lettres de l'alphabet), notre plan qui,
        à chaque lettre d'expéditeur associe une lettre de destinataire
    Sorties:
        - Booléen, True si tous les éléments de plan sont parcourus en
          partant de l'expéditeur d'origine, False sinon
    Rôle:
    Prend en paramètre un dictionnaire 'plan' correspondant à un plan
    d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False
    sinon.
    """
    expediteur = "A"
    destinataire = plan[expediteur]
    nb_destinataires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1

    return nb_destinataires == len(plan)


# False
print(
    est_cyclique({"A": "E", "F": "A", "C": "D", "E": "B", "B": "F", "D": "C"})
)
print(
    est_cyclique({"A": "B", "F": "A", "C": "D", "E": "C", "B": "F", "D": "E"})
)

# True
print(
    est_cyclique({"A": "E", "F": "C", "C": "D", "E": "B", "B": "F", "D": "A"})
)
print(
    est_cyclique({"A": "B", "F": "C", "C": "D", "E": "A", "B": "F", "D": "E"})
)
