tipo = input()
if tipo == 'Q' or tipo == 'R' or tipo == 'C':
    if tipo == 'Q':
        lado = float(input())
        areaQ = lado ** 2
        perimQ = lado * 4
        print(f'{areaQ:.2f}\n{perimQ:.2f}')
    elif tipo == 'R':
        larg = float(input())
        alt = float(input())
        areaR = larg * alt
        perimR = (larg*2) + (alt*2)
        print(f'{areaR:.2f}\n{perimR:.2f}')
    elif tipo == 'C':
        raio = float(input())
        pi = 3.14
        areaC = pi * raio ** 2
        perimC = 2 * pi * raio
        print(f'{areaC:.2f}\n{perimC:.2f}')
else:
    print('Nenhuma figura selecionada')
