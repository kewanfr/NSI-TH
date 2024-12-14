def min_et_max(tab):
  """
  Entrées: - tab, list de nombres, le tableau de nombres
  Sortie: - dictionnaire contenant le minimum et le maximum du tableau
    Clés:
    'min': nombre, le minimum du tableau
    'max': nombre, le maximum du tableau
  Rôle: retourne la plus petite et la plus grande valeur d'un tableau
  """
  if type(tab) != list: # On vérifie que tab est une liste
    print("Erreur: Le paramètre tab doit être une liste")
    return {'min': None, 'max': None}
  
  if not all(type(x) == int or type(x) == float for x in tab):
    # On vérifie que tous les éléments de tab sont des nombres
    print("Erreur: Le tableau ne doit contenir que des nombres")
    return {'min': None, 'max': None}
  
  if len(tab) == 0:
    # Si le tableau est vide, les valeurs de min et max sont None
    return {'min': None, 'max': None}
  
  # On initialise des variables par défaut pour le min et le max
  result = {'min': tab[0], 'max': tab[0]}

  for nombre in tab: # On parcourt les nombres de tab 
    if nombre > result['max']: # Si le nombre est le max
      result['max'] = nombre # On change la valeur du maximum

    if nombre < result['min']: # Pareil pour le minimum
      result['min'] = nombre

  return result


print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3]))
print(min_et_max([-1, -1, -1, -1, -1]))
# print(min_et_max(0))
# print(min_et_max(0))