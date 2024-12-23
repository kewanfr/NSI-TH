class Carte:
  def __init__(self, c, v):
    """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
    self.couleur = c
    self.valeur = v

  def get_valeur(self):
    """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
    valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
    return valeurs[self.valeur - 1]

  def get_couleur(self):
    """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trèfle). """
    couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
    return couleurs[self.couleur - 1]

class Paquet_de_cartes:
  def __init__(self):
    """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
        rangés par valeurs croissantes en commençant par pique, puis coeur,
        carreau et tréfle. """
    self.contenu = [] # On initialiste une liste de cartes
    for couleur in range(1, 5):
      # On itère sur les 4 couleurs de cartes
      for valeur in range(1, 14):
        # On itère sur les 13 valeurs de cartes

        self.contenu.append(Carte(couleur, valeur))
        # On ajoute la carte dans la liste

  def get_carte(self, pos):
    """ Renvoie la carte qui se trouve à la position pos (entier compris entre 0 et 51). """
    assert pos < len(self.contenu), "paramètre pos invalide"
    # On vérifie que le paramètre pos est correct

    return self.contenu[pos] # On renvoie la carte à la position pos



jeu = Paquet_de_cartes()

carte1 = jeu.get_carte(20)
print(carte1.get_valeur() + " de " + carte1.get_couleur())

carte2 = jeu.get_carte(0)
print(carte2.get_valeur()+ " de " + carte2.get_couleur())

carte3 = jeu.get_carte(52)
