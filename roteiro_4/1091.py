n = int(input())
soma = ''
x = 0

for i in range(n):
  if i == 0:
    x += 1/4
    soma += f'1/{i+4} + '
  elif i%2!=0:
    x += 1
    soma += f'1 + '
  else:
    x += (i+1)/((i+2)*2)
    soma += f'{i+1}/{(i+2)*2} + '

print(f'{x:.2f}')
if soma != '':
  print(soma[0:-3])
