def ajoute_dictionnaires(d1, d2):
  """
  Entrées: 
    - d1 et d2, dictionnaires, dont les clés sont des nombres,
      dictionnaires à additionner
  Sorties: d, dictionnaire, résultat de l'addition de d1 et d2
  Rôle: Ajoute 2 dictionnaires.
        Si une clé est présente 2 fois, sa valeur est la somme des 2
  """
  new_dict = {} # On créé un dictionnaire vide
  for key in d1: 
    if key in d2: # Si la clé est présente dans les 2 dictionnaires
      new_dict[key] = d1[key] + d2[key] # On fais la somme
    else:
      new_dict[key] = d1[key] # Sinon, on ajoute uniquement la valeur
  
  for key in d2:
    # On doit aussi ajouter les clés qui sont uniquement dans d2
    if not key in d1: 
      new_dict[key] = d2[key]

  return new_dict


print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))