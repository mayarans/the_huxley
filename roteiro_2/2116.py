carne = input()

if carne == 'C' or carne == 'BF' or carne == 'BS':
  paoDeAlho = input()
  bebidaAdulto = input()
  bebidaKid = input()
  quantKid = int(input())
  quantAdulto = int(input())
  if bebidaAdulto == 'S':
    x = 2*8*quantAdulto
  elif bebidaAdulto == 'N':
    x = 0
  if bebidaKid == 'S':
    y = 0.5*6*quantKid
  elif bebidaKid == 'N': 
    y = 0
  if paoDeAlho == 'S':
    if carne == 'C':
      calculoC = (6.4 + 1.8 + 1.5)*quantAdulto + (6.4 * quantKid) + x + y
      print(f'R$: {calculoC:.2f}')
    elif carne == 'BF':
      calculoBF = (8 + 2.7)*quantAdulto + (6.4* quantKid) + x + y
      print(f'R$: {calculoBF:.2f}')
    elif carne == 'BS':
      calculoBS = (8 + 2.25)*quantAdulto + (6.4 * quantKid) + x + y
      print(f'R$: {calculoBS:.2f}')
  elif paoDeAlho == 'N':
    if carne == 'C':
      calculoC = (6.4 + 1.8 + 1.5)*quantAdulto + (6.4 * quantKid) + x + y
      descontoC = calculoC - calculoC *0.02
      print(f'R$: {descontoC:.2f}')
    elif carne == 'BF':
      calculoBF = (8 + 2.7)*quantAdulto + (6.4* quantKid) + x + y
      descontoBF = calculoBF - calculoBF *0.02
      print(f'R$: {descontoBF:.2f}')
    elif carne == 'BS':
      calculoBS = (8 + 2.25)*quantAdulto + (6.4 * quantKid) + x + y
      descontoBS = calculoBS - calculoBS *0.02
      print(f'R$: {descontoBS:.2f}')
else:
  print('Opção inválida.')
