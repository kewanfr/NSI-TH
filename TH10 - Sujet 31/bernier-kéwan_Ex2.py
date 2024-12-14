def binaire(a):
  """
  Entrées: 
    - a, un int, le nombre en base 10 à convertir en binaire
  Sorties:
    - bin_a, str, le nombre en base 2
  Rôle: convertir un nombre décimal (base 10) en binaire (base 2)
  """
  if type(a) != int: # a doit être un entier
    print("Erreur: a doit être un entier")
    return None
  
  if a < 0: # Si a est négatif, on ne peut pas le convertir
    print("Erreur: a doit être positif")
    return None
  
  if a == 0: # Cas particulier, 0 en binaire est 0
    return "0"

  bin_a = str(a%2) # Le reste de la division euclidienne
  a = a // 2 # Le résultat de la division
  while a > 0:
    bin_a = str(a%2) + bin_a # On ajoute le reste au début du binaire
    a = a // 2
  return bin_a

print(binaire(0))
print(binaire(77))
print(binaire(31))
print(binaire(-1))
print(binaire(1))
print(binaire("31"))
