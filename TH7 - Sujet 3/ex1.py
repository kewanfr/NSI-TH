def moyenne(liste_notes):
  """
  Entrées: list_notes: list de tuples de float (valeur, coefficient),
  la liste des notes
  Sortie: float, la moyenne pondérée ou None
  Rôle: Calcule et renvoie la moyenne pondérée d'une liste de notes
  """
  # On vérifie les préconditions
  if type(liste_notes) != list:
    print("Erreur: la liste de notes doit être une liste")
    return None
  
  if len(liste_notes) <= 0:
    print("Erreur: la liste de notes ne doit pas etre vide")
    return None
  
  somme = 0
  somme_coefs = 0
  for (valeur, coefficient) in liste_notes: # On itère dans liste_notes
  # et on destructure le tuple de la note et le coeff
    somme += valeur * coefficient
    # On ajoute la note pondérée par le coeff à la somme
    somme_coefs += coefficient # On ajoute le coeff à la somme
    
  if somme_coefs == 0: # On ne peut pas diviser par 0
    print("Erreur: La somme des coefficients doit être positive")
    return None

  return somme / somme_coefs # On renvoie et calcule la moyenne


print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))