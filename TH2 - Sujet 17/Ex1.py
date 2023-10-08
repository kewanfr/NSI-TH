def moyenne(liste_notes):
  """
  Entrées: liste_notes un tableau de tuples (note, coefficient)
  Sortie: un flottant
  Rôle: Renvoie la moyenne pondérée des notes de liste_notes
  Précondition: 
    - liste_notes doit être non vide
    - note est un flottant compris entre 0 et 20
    - coefficient est un entier strictement positif
  Postcondition:
    - la moyenne est un flottant compris entre 0 et 20
  """
  assert liste_notes != [], "liste_notes doit être un tableau non vide"
  somme = 0
  coefs = 0
  for note, coef in liste_notes: # on itère sur chaque note et on prends la note et le coef
    assert type(note) in [int, float], "les notes doivent être des flottants"
    assert 0 <= note <= 20, "note doit être compmris entre 0 et 20"
    assert coef > 0, "le coefficient doit être être strictement positif"
    somme += note*coef # On fait la somme des notes pondérées
    coefs += coef
  moyenne = somme/coefs # On calcule la moyenne
  return moyenne
  
print(moyenne([(15, 2), (9,1), (12, 3)]))