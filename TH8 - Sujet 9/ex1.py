def multiplication(n1, n2):
  """
  Entrées: - n1, de type int, le premier nombre entier
           - n2, de type int, le second nombre entier
  Sorties: int, résultat du produit de n1 et n2
  Rôle: Calcule et renvoie le résultat de la multiplication
  de n1 et n2
  """
  produit = 0

  # Si l'un des deux nombres est nul, le produit est null
  if n1 == 0 or n2 == 0: 
    return produit

  est_negatif = (n1 < 0 or n2 < 0) and (n1 >= 0 or n2 >= 0)
  # On met un booléen si le résultat doit être négatif

  # On prend la valeur absolue des deux nombres
  if n1 < 0:
    n1 = -n1

  if n2 < 0:
    n2 = -n2
  
  # On fait la multiplication
  for _ in range(n1):
    produit += n2
  
  # On remet le signe négatif si le résultat doit l'être
  if est_negatif:
    produit = -produit

  return produit

print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(6, -2))
print(multiplication(-2, 0))
print(multiplication(0, 12))