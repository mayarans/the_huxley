def multiplicacaoPorSoma(n1, n2):
  soma = 0
  for i in range(abs(n1)):
    soma += abs(n2)
  if (n1 < 0 and n2 < 0) or (n1>=0 and n2>=0):
    return soma
  elif n1<0 or n2<0:
    return soma*(-1)

n1 = int(input())
n2 = int(input())
print(multiplicacaoPorSoma(n1, n2))