time = input()

if time == 'GSW' or time == 'HOU' or time == 'CLE' or time == 'BOS':
  nome = input()
  tentados2 = int(input())
  convertidos2 = int(input())
  tentados3 = int(input())
  convertidos3 = int(input())

  percentual2 = (convertidos2/tentados2)*100
  percentual3 = (convertidos3/tentados3)*100
  pontos = convertidos2 * 2 + convertidos3 * 3

  if pontos > 30:
    print(f'O time {time} estah jogando, e {nome} estah indo bem.')
  elif percentual2 > 50 and tentados2 > 10:
    print(f'O time {time} estah jogando, e {nome} estah indo bem.')
  elif percentual3 > 40 and tentados3 > 7:
    print(f'O time {time} estah jogando, e {nome} estah indo bem.')
  else:
    print(f'O time {time} estah jogando, mas {nome} nao estah indo bem.')
else:
  print('Nenhum time de interesse jogando.')
