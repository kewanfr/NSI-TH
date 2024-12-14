Urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'A']

def depouille(urne):
  """
  Entrée: 
    - urne: list de str : Contient les bulletins de vote
  Sortie: 
    - resultat: dict de forme {candidat(str): nb_votes(int)} : Nombre de votes pour chaque candidat
  Rôle: Compte le nombre de votes pour chaque candidat
  """
  resultat = {} # Dictionnaire vide
  for bulletin in urne: 
    if bulletin in resultat: # Si le candidat a déjà une clé dans le dict resultat, alors on incrémente son nombre de votes de 1
      resultat[bulletin] = resultat[bulletin] + 1
    else: # Sinon on lui créé une clé en lui mettant un seul vote
      resultat[bulletin] = 1
  return resultat
 
def vainqueur(election):
  """
  Entrée:
    - election : dict de forme {candidat(str): nb_votes(int)} : Nombre de votes pour chaque candidat
  Sortie:
    - liste_finale : list de str : Liste des candidats ayant le plus de votes
  Rôle: Renvoie le ou les candidats avec le plus de votes
  """
  vainqueur = '' # On initialise le vainqueur
  nmax = 0 # Le nombres de votes maximum 
  for candidat in election: # On parcourt chaque candidat
    if election[candidat] > nmax: # Si son nombre de votes est le plus grand, on le définit comme vainqueur
      nmax = election[candidat] # Le nombre de votes max est mis à jour
      vainqueur = candidat # Le nom du vainqueur aussi
  liste_finale = [nom for nom in election if election[nom] == nmax] # On créé un liste, on y mets les noms de chaque candidat ayant le nombre de voix maximum (c'est à dire les vainqueurs)
  return liste_finale

print(depouille(Urne))
print(vainqueur(depouille(Urne)))