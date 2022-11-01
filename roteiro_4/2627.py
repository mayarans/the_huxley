quant = int(input())
resultado = ''

for i in range(quant):
  x = float(input())
  if i < quant:
    resultado += f'{x:.3f} '
  else:
    resultado += f'{x:.3f}'
print(resultado)
