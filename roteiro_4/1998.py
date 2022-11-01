n1 = 0
n2 = 0
while n1 < 1 or n1 > 9:
  n1 = int(input())
  if n1 < 1 or n1 > 9:
    print('Insira um número inicial entre 1 e 9')
while n2 < 1 or n2 > 9:
  n2 = int(input())
  if n2 < 1 or n2 > 9:
    print('Insira um número final entre 1 e 9')
if n1>n2:
  print('Nenhuma tabuada nesse intervalo')
calculo = ''
cont = 0
for i in range (n1, n2+1):
  if cont == 9:
    print()
    cont = 0
  for a in range (1, 10):
    print(f'{i} x {a} = {i*a}')
    cont+=1
