temp = float(input())
doente = input()
if doente == 'S' or doente == 'N':
    if temp >= 37 and doente == 'S':
        print('Exames Especiais')
    elif temp >= 37 and doente == 'N':
        print('Exames Basicos')
    elif temp < 37 and doente == 'N':
        print('Liberado')
    elif temp < 37 and doente == 'S':
        print('Exames Basicos')
else: 
    print('Erro')
