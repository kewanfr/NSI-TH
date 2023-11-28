coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
  """
  Entrées: - dessin, list de list de 0 ou 1, tableau du dessin
  Sorties: Aucune
  Rôle: Affiche une grille : les 1 sont représentés par des " *", 
  les 0 par deux espaces "  "
  """

  for ligne in dessin:
    for col in ligne: # Pour chaque élément du dessin
      # On affiche une
      if col == 1:
        print(" *", end= "")
        # end="" permet de ne pas avoir de saut de ligne 
      else:
        print("  ", end= "")
    print()

def zoomListe(liste_depart, k):
  """
  Entrées: - liste_depart, list de 0 ou 1, la liste de départ
           - k, int, le coefficient de zoom
  Sorties: list de int, de 0 ou 1, une liste contenant k fois
  chaque élément de liste_depart
  Rôle: Zoom de k fois la liste_depart
  """
  liste_zoom = []

  for elt in liste_depart:
    # On répète k fois chaque élément de la ligne
    for i in range(k):
      liste_zoom.append(elt)
  return liste_zoom

def zoomDessin(grille, k):
  """
  Entrées: - grille, list de list de 0 ou 1, la grille de dessin
  Sorties: list de list de 0 ou 1, le dessin zoomé
  Rôle: Renvoie une grille où les lignes sont zoomées k fois
  ET répétées k fois
  """
  '''renvoie une grille où les lignes sont zoomées k fois
  ET répétées k fois'''
  grille_zoom = []
  for elt in grille: # on itère sur chaque ligne de la grille
    liste_zoom = zoomListe(elt, k)
    # On répète k fois les éléments de la ligne

    for i in range(k): # Et on la répète k fois
      grille_zoom.append(liste_zoom)
  return grille_zoom


affiche(coeur)
affiche(zoomDessin(coeur, 3))