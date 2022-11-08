n = int(input())
lista = list(map(int, input().split()))

listaOrdenada = sorted(lista)

for i in lista:
    if i == listaOrdenada[0]:
        print(f'Menor valor: {listaOrdenada[0]}\nPosicao: {lista.index(listaOrdenada[0])}')