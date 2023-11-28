pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
  """
  Entrées: somme_due, de type int, la somme que le client doit payer
           somme_versee, de type int, la somme que le client a déjà versée
  Sorties: rendu, de type list de int, la liste des pièces à rendre
  Rôle: Renvoie la liste des pièces à rendre au client
  """
  #  si ce ne sont pas des entiers, on renvoie une liste vide
  if type(somme_due) != int or type(somme_versee) != int:
    print("Les sommes doivent être des entiers")
    return []

  rendu = []
  a_rendre = somme_versee - somme_due # La somme a rendre 
  if a_rendre <= 0: # Si la somme à rendre est négative ou nulle, alors le client a payé assez
    return rendu
  
  i = len(pieces) - 1 # On commence par la plus grosse pièce
  while a_rendre > 0 : # Tant qu'il reste de l'argent à rendre
    if pieces[i] <= a_rendre: # Si la pièce est inférieure à la somme à rendre
      rendu.append(pieces[i]) # On ajoute la pièce à la liste
      a_rendre = a_rendre - pieces[i] # On retire la pièce à la somme à rendre
    else:
      i = i - 1 # Sinon on passe à la pièce suivante
  return rendu


print(rendu_monnaie(700, 700))
print(rendu_monnaie(102, 500))