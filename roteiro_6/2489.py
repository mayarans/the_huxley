listaCoisasParaFazer = []
listaCoisasFeitas = []
listaDeletar = []

quantParaFazer = int(input())
for i in range(quantParaFazer):
  coisasParaFazer = input()
  listaCoisasParaFazer.append(coisasParaFazer)

quantJaFez = int(input())
for i in range(quantJaFez):
  coisasFeitas = input()
  listaCoisasFeitas.append(coisasFeitas)

for a in range(len(listaCoisasFeitas)):
  for i in range(len(listaCoisasParaFazer)):
    if listaCoisasFeitas[a] == listaCoisasParaFazer[i]:
      deletar = listaCoisasParaFazer[i]
      listaDeletar.append(deletar)

for i in listaDeletar:
  listaCoisasParaFazer.remove(i)

if listaCoisasParaFazer == []:
  print('Smelly Cat, Smelly Cat, what are they feeding you?')
else:
  print(f'Ainda falta(m) {len(listaCoisasParaFazer)} objetivo(s)!')
  for i in listaCoisasParaFazer:
    print(i)