def inverse_chaine(chaine):
  """
  Entrées: - chaine, un str, notre chaine de caractères à inverser
  Sortie: str, la chaine inversée
  Role: Renverse l'ordre des caractères d'une chaîne de caractères
  et renvoie la chaîne inversée
  """
  result = "" # On initie une chaine de caractères vide
  for caractere in chaine: # On itère sur chaque caractère de la str
    # On ajoute le caractère au début de la chaine
    result = caractere + result 
  return result

def est_palindrome(chaine):
  """
  Entrées: - chaine, un str, la chaine de caractères à tester
    si c'est un palindrome
  Sorties: Boolean, True si chaine est un palindrome, False sinon
  Role: Teste si une chaîne de caractères est un palindrome
  """
  if len(chaine) == 0:
    print("La chaine est vide")
    return False
  
  inverse = inverse_chaine(chaine) # Récupère la chaine inversée
  # Si la chaine inversée est la chaine de base, c'est un palindrome
  return inverse == chaine

def est_nbre_palindrome(nbre):
  """
  Entrées: - nbre, entier, le nombre à tester
  Sorties: Booléen, True si le nombre est palindrome, False sinon
  Rôle: Teste si un nombre est palindrome
  """

  if type(nbre) == str:
    return est_palindrome(nbre)
  
  chaine = str(nbre) # Convertir le nombre en chaîne de caractères
  return est_palindrome(chaine)
