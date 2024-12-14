class Noeud:
    def __init__(self, etiquette, gauche, droit):
        # Initialisation de l'arbre, avec les variables passés en paramètre
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit


def hauteur(a):
    """
    Entrées: - a, objet Noeud, arbre
    Sorties: - int, hauteur de l'arbre a
    Rôle: Fonction récursive pour obtenir l'hauteur d'un arbre
    """
    # Cas de base: Si l'arbre est vide, sa hauteur est -1
    if a is None:
        return -1
    # Sinon, on renvoie la hauteur la plus grande entre
    # le sous-arbre gauche et le sous-arbre droit
    else:
        return 1 + max(hauteur(a.droit), hauteur(a.gauche))


def taille(a):
    """
    Entrées: - a, objet Noeud, arbre
    Sorties: - int, taille de l'arbre a
    Rôle: Fonction récursive pour renvoyer la taille d'un arbre
    """
    # Cas de base: Si l'arbre est vide, sa taille est de 0
    if a is None:
        return 0
    # Sinon, on renvoie la somme du sous-arbre gauche
    # et du sous-arbre droit
    else:
        return 1 + taille(a.gauche) + taille(a.droit)


# Exemple du sujet à tester
ARBRE_A = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))


# print(hauteur(n))
print(hauteur(ARBRE_A))
print(taille(ARBRE_A))
print(hauteur(None))
print(taille(None))

print(hauteur(Noeud(1, None, None)))
print(taille(Noeud(1, None, None)))
