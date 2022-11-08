gabarito = input()
listaNomes = []
listaRespostas = []
cont = 0
aprovados = 0
maiorCont = 0 

while True:
  nome = input()
  if nome == 'sair':
    break
  else:
    listaNomes.append(nome)
    resposta = input()
    for i in range(5):
      if gabarito[i] == resposta[i]:
        cont+=1
    listaRespostas.append(cont)
    if cont >= maiorCont:
      aluno = f'{nome}'
      maiorCont = cont
    cont = 0

print(listaNomes)
print(listaRespostas) 

media = 20*(sum(listaRespostas))/(len(listaRespostas))
print(media)
for i in listaRespostas:
  if i*20 > media:
    aprovados += 1
print(aprovados)
print(aluno)