crimeDelator = input()
if crimeDelator == 'roubo' or crimeDelator == 'tráfico' or crimeDelator == 'homicídio':
  if crimeDelator == 'roubo' or crimeDelator == 'tráfico':
    valorCrimeDelator = int(input())
  crimeDelatado = input()
  if crimeDelatado == 'roubo' or crimeDelatado == 'tráfico' or crimeDelatado == 'homicídio':
    if crimeDelatado == 'roubo' or crimeDelatado == 'tráfico':
      valorCrimeDelatado = int(input())
    if crimeDelatado == 'homicídio' and crimeDelator == 'roubo':
      print('Delação concedida.')
    elif crimeDelatado == 'homicídio' and crimeDelator == 'tráfico':
      print('Delação concedida.')
    elif crimeDelator == crimeDelatado == 'roubo':
      if valorCrimeDelatado > (valorCrimeDelator*5):
        print('Delação concedida.')
      else:
        print('Delação rejeitada.')
    elif crimeDelator == 'roubo' and crimeDelatado == 'tráfico':
      if valorCrimeDelatado > (valorCrimeDelator*3):
        print('Delação concedida.')
      else: 
        print('Delação rejeitada.')
    elif crimeDelator == 'tráfico' and crimeDelatado == 'tráfico':
      if valorCrimeDelatado > (valorCrimeDelator*5):
        print('Delação concedida.')
      else:
        print('Delação rejeitada.')
    elif crimeDelator == crimeDelatado == 'homicídio':
      print('Delação concedida.')
    else:
      print('Delação rejeitada.')
  else:
    print('Crime inválido.')
else:
  print('Crime inválido.')





