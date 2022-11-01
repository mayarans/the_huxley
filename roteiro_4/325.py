n = int(input())
resultado = ''

for i in range (1, n+1):
  resultado = ''
  for a in range (1, 4):
    x = i**a
    resultado += f'{x} '
  print(resultado[0:-1])
 