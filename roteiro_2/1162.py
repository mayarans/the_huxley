ataque = input()
defesa = input()

if ataque == 'Planta':
  if defesa == 'Planta':
    print('Empate')
  elif defesa == 'Fogo':
    print('Desvantagem')
  elif defesa == 'Agua':
    print('Vantagem')
elif ataque == 'Fogo':
  if defesa == 'Planta':
    print('Vantagem')
  elif defesa == 'Fogo':
    print('Empate')
  elif defesa == 'Agua':
    print('Desvantagem')
elif ataque == 'Agua':
  if defesa == 'Planta':
    print('Desvantagem')
  elif defesa == 'Fogo':
    print('Vantagem')
  elif defesa == 'Agua':
    print('Empate')
