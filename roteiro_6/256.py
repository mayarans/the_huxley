n1 = int(input())
lista1 = []
lista2 = []

for i in range(n1):
    valores = int(input())
    lista1.append(valores)

for i in range(n1):
    valores = int(input())
    lista2.append(valores)

for i in range(n1):
    print(f'{lista1[i]}\n{lista2[i]}')