def chercher(tab, n, i, j):
  """
  Entrées:
    - tab, list de int, le tableau dans lequel s'effectue la recherche
    - n, int, l'entier à chercher dans le tableau
    - i l'indice de début de la partie du tableau où s'effectue le recherche
    - j l'indice de fin de la parie du tableau où s'effectue la recherche
  Sorties: indice où la valeur n apparait dans tab, ou None.
  Rôle: Renvoie un indice où la valeur n apparait dans tab, par recherche dichotomique récursive
  """
  if i < 0 or j > len(tab): # Si les indices sont hors du tableau
    return None
  elif i > j:
    return None
  
  m = (i+j) // 2 # Le milieu entre l'indice de début et fin

  if tab[m] < n:
    # Si la valeur du milieu est + petite que celle qu'on cherche
    # On cherche l'élément dans la partie supérieure de la liste
    return chercher(tab, n, m+1, j)
  elif tab[m] > n:
    # Si la valeur du milieu est + grande que celle qu'on cherche
    # On cherche l'élément dans la partie inférerieure de la liste
    return chercher(tab, n, i, m-1)
  else: # Sinon, tab[m] == n, donc on renvoie l'indice
    return m
  
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))