n1 = int(input())
resultado = ''
if n1 > 0:
    l1 = []
    for i in range(n1):
        valor = int(input())
        l1.append(valor)

    n2 = int(input())
    if n2 > 0:
        l2 = []
        for i in range(n2):
            valor = int(input())
            l2.append(valor)
        lista = l1 + l2
        for i in lista:
            resultado += f'{i} '
        print(resultado)
    else:
        print('Erro - A lista deve ter pelo menos 1 elemento.')
else:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
