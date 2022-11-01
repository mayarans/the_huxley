cont = 0
soma = 0
for i in range (7):
    n = int(input())
    soma+=n
    if n >= 100:
        cont += 1
media = soma/7
print(f'{cont}\n{media:.0f}')
