def recherche(elt, tab):
  """
  Entrées: elt de type int ou float, élément qu'on recherche
           tab de type list de int ou float, liste dans laquelle on recherche le nombre d'occurrences de elt dans tab
  Sorties: compteur de type int, nombre d'occurrences de elt dans tab
  Rôle: Renvoie le nombre d’occurrences d’un élément dans une liste, ou -1 si il y a une erreur
  """
  if type(elt) != int and type(elt) != float: # On vérifie que l'élément est un nombre
    print("L'élément doit être un entier ou un flottant")
    return -1
  
  if type(tab) != list: # On vérifie que tab est une liste
    print("Tab doit etre une liste")
    return -1
  
  nb = 0
  for i in tab: # On itère à travers chaque élément du tableau
    if i == elt: # Si c'est l'élément, on incrémente le compteur de 1
      nb += 1
  return nb

print(recherche(5, []))
print(recherche(5, [-2, 3, 4, 8]))
print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5, [-2, 5, 3, 5, 4, 5]))