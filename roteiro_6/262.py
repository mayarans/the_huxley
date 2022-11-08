n = int(input())
lista = []
acima = 0
abaixo = 0

for i in range(n):
    nota = int(input())
    lista.append(nota)

media = sum(lista)/n

for i in range(len(lista)):
    if lista[i] > media + (0.10*media):
        acima += 1
    elif lista[i] < media - (0.10*media):
        abaixo += 1

print(f'{media:.2f}\n{acima}\n{abaixo}')