t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve, date):
  """
  Entrées: 
    - releve, list de float, le relevé des températures
    - date, list de int, le tableau des années
  Sortie: tuple:
    - float, température minimale ou None
    - int, année correspondante ou None
  Rôle: Renvoie la plus petite valeur de température relevée
  avec son année correspondante
  """

  if type(releve) != list or type(date) != list:
    print("Les entrées doivent être des listes")
    return (None, None)
  
  if len(releve) < 1 or len(date) < 1:
    print("Les listes ne doivent pas etre vides")
    return (None, None)
    
  if len(releve) != len(date):
    print("Les listes n'ont pas la même taille")
    return (None, None)
  
  
  # On définit une variable pour la valeur la plus petite
  val_mini = releve[0]
  date_mini = date[0]

  for i in range(len(releve)): # On itère sur chaque valeur
    if releve[i] < val_mini: # Si elle est plus petite que l'ancienne

      # On la définit en tant que valeur la plus petite
      val_mini = releve[i]

      date_mini = date[i] # On définit son année également
  return (val_mini, date_mini) # On renvoie un tuple

print(mini(t_moy, annees))