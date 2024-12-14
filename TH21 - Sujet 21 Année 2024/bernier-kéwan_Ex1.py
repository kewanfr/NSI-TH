def recherche_motif(motif, texte):
    """
    Entrées: 
        - motif, str, le motif à chercher dans le texte
        - texte, str, le texte dans lequel chercher le motif
    Sorties:
        - list de int, liste des positions où se trouve le motif 
    Role: Recherche un motif dans un texte avec la méthode naïve et
        renvoie ses positions
        
    Préconditions:
        - motif et texte sont des str
        - motif et texte ne sont pas vides
        - motif est plus petit ou égal à texte
    Postconditions:
        - Renvoie la liste de positions des occurences du motif dans le texte
    """

    # Vérifie que c'est bien des chaines de caractère
    if not isinstance(motif, str) or not isinstance(texte, str):
        # Sinon affiche une erreur
        print("Erreur: Motif et texte doivent être des str !")
        return None
    
    if motif == "" or texte == "":
        # Si motif ou texte est vide, on ne peut pas chercher le motif
        print("Erreur: Motif et texte ne peuvent pas être vides !")
        return None
    
    if len(motif) > len(texte):
        # Si le motif est plus grand que le texte
        # on ne peut pas chercher le motif
        print("Erreur: Le motif ne peut pas être plus grand que le texte !")
        return None

    liste_positions = [] # Initialise la liste des positions

    # Itère à travers chaque caractère du texte
    for i in range(len(texte)):
        # Si les n caractères du texte à partir de i sont égaux à motif
        if texte[i:i+len(motif)] == motif:
            # Il y a le motif dans le texte
            # donc on ajoute l'indice à la liste des positions
            liste_positions.append(i)

    return liste_positions

print(recherche_motif("ab", ""))
print(recherche_motif("ab", "cdcdcdcd"))
print(recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))

print(recherche_motif("4", 456334))
print(recherche_motif(8, "8549688"))