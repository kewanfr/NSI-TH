from random import randint
  
def nbre_coups():
  """
  Entrées: Aucune
  Sorties: n, entier, nombre de coups pour voir toutes les cases
  Rôle: Simule un jeu avec 12 cases, et renvoie le nombre de coups
        nécessaires pour passer sur chacune d'entre elle.
        En tirant aléatoirement un dé à 6 faces à chaque tour.
  """
  n = 0 # Nombre de coups
  cases_vues = [0]
  case_en_cours = 0
  nbre_casses = 12
  while len(cases_vues) < nbre_casses:
    x = randint(1, 6)

    # Case suivante: case actuelle + x (% 12 pour rester dans le jeu)
    case_en_cours = (case_en_cours + x) % nbre_casses

    if case_en_cours not in cases_vues:
      cases_vues.append(case_en_cours) # On ajoute la case à la liste
    n = n + 1
  return n

def test_fonction():
  """
  Entrées: Aucune
  Sorties: True ou AssertionError
  Rôle: Teste la fonction nbre_coups, fais la moyenne de 50 essais
        La moyenne doit etre entre 25 et 35. 
        Et la somme entre 1300 et 1750
  """
  sum = 0
  nb = 0
  for _ in range(50):
    nb += 1
    sum += nbre_coups()

  assert 25 <= sum/nb <= 35 and 1300 <= sum <= 1750 and nb == 50
  print("La fonction nbre_coups fonctionne correctement")
  return True

test_fonction()