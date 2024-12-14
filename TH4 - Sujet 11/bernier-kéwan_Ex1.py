def convertir(tab):
  """
  Entrées: tab de type list de int (0 ou 1), notre nombre en binaire
  Sortie: de type int, notre nombre binaire converti en écriture décimale
  Rôle : Renvoie l'écriture décimale de l'entier positif dont la représentation binaire est donnée par le tableau tab
  """
  nb = 0 # Notre somme
  for i in range(len(tab)): # On parcourt chaque bit
    nb += tab[i]*2**(len(tab)-i-1) # 2^{len(tab) - i - 1} est la valeur du bit, on le multiplie à la valeur du bit, si c'est 1 on l'ajoute à la somme, si c'est 0 on ne l'ajoute pas
  return nb

print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))