maiorPonto = 0
menorPonto = 100
total = 0
cont = 0

nome = input()
if nome != 'sair':
    while True:
        cont+=1
        pontos = int(input())
        total += pontos
        if pontos>=maiorPonto:
            x = f'{nome}'
            maiorPonto = pontos
        if pontos <= menorPonto:
            y = f'{nome}'
            menorPonto = pontos
        nome = input()
        if nome == 'sair':
            break
    media = total / cont
    print(y)
    print(x)
    print(f'{media:.2f}')
else:
    print('Nenhum jogador foi registrado.')
