def verifie(tab):
  """
  Entrées: tab un tableau de valeurs numériques
  Sortie: True si le tableau est trié dans l'ordre croissante, False sinon
  Rôle: Vérifie si un tableau de valeurs est trié dans l'ordre croissante
  Précondition: tab contient uniquement des nombres et est non vide
  Postcondition: Renvoie True si le tableau est trié
  """
  if len(tab) <= 0: # Le tableau ne doit pas être vide selon la précondition
    print("Erreur, Le tableau tab doit être non vide")
    return True # Même si le tableau est vide, il est trié
  
  for i in tab: # On effectue un test sur la nature de chaque élément du tableau
    if type(i) not in [int, float]: # Si l'élément n'est pas un entier ou un flottant, on retourne une erreur
      print("Erreur, Toutes les valeurs de tab doivent être des nombres")
      return False
  
    
  for i in range(len(tab) - 1): # On s'arrête à len(tab) - 1 car on compare l'élément actuel avec l'élément suivant, donc au dernier passage, on pourra comparer l'avant dernier et le dernier élément
    if tab[i + 1] < tab[i]: # Si l'élément actuel est plus petit que l'élément suivant, le tableau n'est pas trié
      return False # On renvoie False, si un seul élement n'est pas trié, le tableau entier n'est pas trié
  return True # Si False n'a pas été renvoyé, cela signifie que le tableau est trié

print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))
