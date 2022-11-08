listaNotas = []
listaNomes = []
decrescente = ''
distancia = ''
maiorDistancia = 0

for i in range(5):
    nota = float(input())
    listaNotas.append(nota)
    nome = input()
    listaNomes.append(nome)
listaNotasOrdenadas = sorted(listaNotas)

media = sum(listaNotas)/5

for i in listaNotasOrdenadas[::-1]:
    decrescente += f'{i:.2f} '
    
media = sum(listaNotas)/5

for i in range(len(listaNotas)):
    calculoDistancia = abs(listaNotas[i]-media)
    distancia += f'{calculoDistancia:.2f} '
    if calculoDistancia > maiorDistancia:
        posicaoMaisDistante = listaNotas.index(listaNotas[i])
        pessoaMaisDistante = listaNomes[i]
        maiorDistancia = calculoDistancia
    elif calculoDistancia == 0 and maiorDistancia==0:
        posicaoMaisDistante = listaNotas.index(listaNotas[i])
        pessoaMaisDistante = listaNomes[i]

print(f'{decrescente[0:-1]}')
print(f'{media:.2f}')
print(f'{distancia[0:-1]}')
print(f'{pessoaMaisDistante.title()}')
print(posicaoMaisDistante)