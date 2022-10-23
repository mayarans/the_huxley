idade = int(input())
tipo = input()

if idade <=130 and idade >=0:
  if tipo == 'azar' or tipo == 'mmorpg' or tipo == 'moba' or tipo == 'casual':
    if tipo == 'azar':
      if idade >=21:
        print('Pode entrar!')
      else:
        print('Volte daqui há alguns anos.')
    elif tipo == 'mmorpg':
      if idade >=14:
        print('Pode entrar!')
      else:
        print('Volte daqui há alguns anos.')
    elif tipo == 'moba':
      if idade >=10:
        print('Pode entrar!')
      else:
        print('Volte daqui há alguns anos.')
    elif tipo == 'casual':
      print('Pode entrar!')
  else:
    print('Jogo invalido.')
else:
  print('Idade invalida.')
