continua = 'S'
vendaTotal = 0
valor = 0
avista = 0
cont = 0
cartao = 0
maisJovem = 100
maiorCompra = 0

while continua == 'S':
    vendaTotal +=1
    idade = int(input())
    if idade <= maisJovem:
        maisJovem = idade 
    compra = float(input())
    if compra > maiorCompra:
        maiorCompra = compra
    tipo = input()
    continua = input()
    if tipo == 'V':
        avista += compra
        cont+=1
    elif tipo == 'C':
        cartao += compra

if avista != 0:
    media = avista / cont 
else:
    media = 0

if avista == 0 and cartao == 0 and maiorCompra == 0 and media == 0:
    print(f'0\n0\n0\n0\n0\n0')
elif avista == 0 and media ==0:
    print(f'{vendaTotal}\n0\n{cartao:.2f}\n{maisJovem}\n{maiorCompra:.2f}\n0')
elif avista == 0:
    print(f'{vendaTotal}\n0\n{cartao:.2f}\n{maisJovem}\n{maiorCompra:.2f}\n{media:.2f}')
elif cartao == 0:
    print(f'{vendaTotal}\n{avista:.2f}\n0\n{maisJovem}\n{maiorCompra:.2f}\n{media:.2f}')
elif maiorCompra == 0:
    print(f'{vendaTotal}\n{avista:.2f}\n{cartao:.2f}\n{maisJovem}\n0\n{media:.2f}')
elif media == 0:
    print(f'{vendaTotal}\n{avista:.2f}\n{cartao:.2f}\n{maisJovem}\n{maiorCompra:.2f}\n0')
else:
    print(f'{vendaTotal}\n{avista:.2f}\n{cartao:.2f}\n{maisJovem}\n{maiorCompra:.2f}\n{media:.2f}')
