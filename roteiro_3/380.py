num = 0
votoCinema = 0
votoBoliche = 0

while num < 7:
  num +=1
  passeio = input()
  if passeio == 'CINEMA' or passeio == 'cinema' or passeio == 'Cinema' or paseio == 'CiNeMa' or passeio == 'cInEmA':
    votoCinema += 1
  elif passeio == 'BOLICHE' or passeio == 'boliche' or passeio == 'Boliche' or passeio == 'BoLiChE' or passeio == 'bOlIcHe':
    votoBoliche += 1

if votoBoliche > votoCinema:
  print('BOLICHE')
else:
  print('CINEMA')
