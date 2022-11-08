n = int(input())
lista = list(map(int, input().split()))
cont = 0
valores = ''

listaOrdenada = sorted(lista)

for i in range(len(lista)):
    if lista[i] == listaOrdenada[i]:
        cont += 1
        valores += f'{lista[i]} {i+1}\n'
print(cont)
print(valores)