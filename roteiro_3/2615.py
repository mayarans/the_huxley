divida = int(input())
valorMaximo = int(input())

while divida > 0:
    print(f'(antes) {divida}')
    divida = divida - valorMaximo
    if valorMaximo > divida:
        print('(depois) 0')
    else:
        print(f'(depois) {divida}')
