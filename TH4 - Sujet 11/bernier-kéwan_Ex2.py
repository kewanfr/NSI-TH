def tri_insertion(tab):
  """
  Entrées: tab de type list de int, notre tableau à trier
  Sortie: Aucune, le tableau tab est modifié
  Rôle : Trier le tableau tab par ordre croissant en utilisant le tri par insertion
    On définit que le tableau est trié jusqu'à une certaine valeur, à chaque tour on insère la valeur à la bonne place et on augmente de 1 la taille du tableau trié
  """
  if(len(tab) == 0): # Si la liste est vide elle est déjà triée
    return
  
  n = len(tab)
  for i in range(1, n): # On parcourt le tableau à partir de l'index 1, car le premier indice est déjà trié
    valeur_insertion = tab[i] # On stocke la valeur à insérer
    #  la  variable  j  est  utilisée  pour  déterminer  où  placer  la valeur à insérer
    j = i
    # tant qu'on a pas trouvé la place de l'élément à insérer
    # on décale les valeurs du tableau vers la droite
    while j > 0 and valeur_insertion < tab[j-1]: # Tant que la valeur est plus petit que la valeur d'avant, on la décale à gauche et que j est positif (sinon on sort du tableau)
      tab[j] = tab[j-1] # On décale l'élément d'index j-1  à l'index j
      j = j - 1
    tab[j] = valeur_insertion # on peut ainsi mettre la valeur à la bonne place
