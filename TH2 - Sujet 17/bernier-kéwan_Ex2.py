def pascal(n):
  triangle = [[1]] # La première ligne du triangle est toujours égale à [1]
  for k in range(1, n+1): # On itère n fois à partir de 1
    ligne_k = [1] # Le premier élément de la ligne est 1
    for i in range(1, k): # On itère k fois mais comme on commence à 1 on ne le fera pas quant k = 1
      ligne_k.append(triangle[k-1][i-1] + triangle[k-1][i])
    ligne_k.append(1) # Le dernier nombre est toujours 1 également
    triangle.append(ligne_k)
  return triangle

print(pascal(4))
print(pascal(5))