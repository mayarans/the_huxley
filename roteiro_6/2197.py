n = int(input())
posicao = []
caracter = []
resultado = ''

for i in range(n):
    x = input().split()
    posicao.append(int(x[0]))
    caracter.append(x[1])

for i in range(1, (len(posicao))+1):
    for a in posicao:
        if i == a:

            resultado += f'{caracter[posicao.index(a)]}'

print(resultado)
