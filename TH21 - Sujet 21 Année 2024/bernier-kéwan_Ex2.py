    """
    Entrées:
        - adj, list de list de int, listes d'adjacence du graphe
        - x, int, un sommet du graphe
        - acc, list de int, liste des sommets déjà rencontrés
    Sorties:
        - acc est modifié avec les sommets rencontrés lors du parcours
        depuis x
    Role: Réalise un parcours en profondeur récursif du graphe donné
        par les listes d'adjacence adj depuis le sommet x

    Préconditions:
        - x est un sommet du graphe
        - acc est une liste de sommets
    Postconditions:
        - acc contient les sommets accessibles depuis x
    """
def parcours(adj, x, acc):
    if x not in acc:
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    """
    Entrées:
        - adj, list de list de int, listes d'adjacence du graphe
        - x, int, un sommet du graphe
    Sorties:
        - list de int, liste des sommets accessibles depuis x
    Role: Renvoie la liste des sommets accessibles dans le graphe depuis x

    Préconditions:
        - x est un sommet du graphe
    Postconditions:
        - Renvoie la liste des sommets accessibles depuis x
    """
    acc = [] # Initialise la liste des sommets accessibles
    parcours(adj, x, acc) # Réalise un parcours en profondeur du graphe depuis x
    return acc # Renvoie la liste des sommets accessibles

print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0)) # [0, 1, 2, 3]
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4)) # [4, 5]