def nb_repetitions(elt, tab):
  """
  Entrées:
    - elt, type any, element dont on veut compter le nombre d'occurences
    - tab, list, tableau dans lequel on cherche l'élément
  Sorties: nb, le nombre d'occurences de notre élément
  Rôle: Renvoie le nombre d'occurences d'un élément dans une liste.
  """
  if type(tab) != list: # Tab doit être une liste
    print("Erreur: tab doit être une liste")
    return None

  if len(tab) == 0: # Si tab est vide, il n'y a aucun élément
    return 0
  
  nb = 0 # On initialise un compteur du nombre d'occurences
  for element in tab: # On parcourt tab
    if element == elt: # Si l'élement est présent, on incrémente nb
      nb += 1
  return nb

print(nb_repetitions(5,[2,5,3,5,6,9,5]))
print(nb_repetitions('A',['B','A','B','A','R']))
print(nb_repetitions(12,[1,'!',7,21,36,44]))
print(nb_repetitions(12,1))