dia = input()
preco = float(input())
tipo = input()
nome = input()

if dia == 'sab' and tipo =='prata':
  preco = preco * 3
  print(f'O preco do produto {nome} no dia {dia} eh {preco:.2f}')
elif preco >= 10 and preco <= 100 and dia == 'qui':
  preco = (1/3)*preco
  print(f'O preco do produto {nome} no dia {dia} eh {preco:.2f}')
elif dia == 'sex' and preco >= 10 and preco <= 100:
  preco = (1/3)*preco
  print(f'O preco do produto {nome} no dia {dia} eh {preco:.2f}')
elif tipo == 'ouro' and dia == 'seg' or tipo == 'ouro' and dia == 'ter' or tipo == 'ouro' and dia == 'qua':
  preco = preco * 0.5
  print(f'O preco do produto {nome} no dia {dia} eh {preco:.2f}')
else:
  preco = preco * 2
  print(f'O preco do produto {nome} no dia {dia} eh {preco:.2f}')
  