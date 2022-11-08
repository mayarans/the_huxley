popInicial = int(input())
anoInicial = int(input())
razao = int(input())
anoFinal = int(input())

anos = [anoInicial]
populacoes = [popInicial]

calculo = popInicial 
for ano in range(anoInicial + 1, anoFinal+1):
  anos.append(ano)
  calculo *= ((razao/100) + 1)
  populacoes.append(int(calculo))

for i in range(len(anos)):
  print(f'{anos[i]} {populacoes[i]}')
