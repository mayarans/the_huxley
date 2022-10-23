salario = float(input())
comprometido = float(input())
limite = salario * 0.3
x = limite - comprometido 

if comprometido < limite:
  print(f'{x:.2f}')
else:
  print('0.00')
