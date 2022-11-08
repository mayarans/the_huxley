listaPar = []
listaImpar = []


for i in range(15):
    numero = int(input())
    if numero % 2 == 0:
        listaPar.append(numero)
        if len(listaPar) == 5:
            for i in range(5):
                print(f'par[{i}] = {listaPar[i]}')
            listaPar = []
    else:
        listaImpar.append(numero)
        if len(listaImpar) == 5:
            for i in range(5):
                print(f'impar[{i}] = {listaImpar[i]}')
            listaImpar = []

if listaImpar != []:
    for i in range(len(listaImpar)):
        print(f'impar[{i}] = {listaImpar[i]}')
if listaPar != []:
    for i in range(len(listaPar)):
        print(f'par[{i}] = {listaPar[i]}')