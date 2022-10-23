escala = input()
if escala == 'C':
    num = float(input())
    if num >= -273.15:
        CParaF = ((num/5)*9)+32
        CParaK = num + 273.15
        print(f'{CParaF:.2f} F\n{CParaK:.2f} K')
    else:
        print('Valor de temperatura abaixo do minimo')
elif escala == 'F':
    num = float(input())
    if num >= -459.67:
        FParaC = ((num - 32)/9)*5
        FParaK = (((num-32)/9)*5)+273.15
        print(f'{FParaC:.2f} C\n{FParaK:.2f} K')
    else:
        print('Valor de temperatura abaixo do minimo')
elif escala == 'K':
    num = float(input())
    if num >= 0.0:
        KParaC = num-273.15
        KParaF = (((num-273.15)/5)*9)+32
        print(f'{KParaC:.2f} C\n{KParaF:.2f} F')
    else:
        print('Valor de temperatura abaixo do minimo')
