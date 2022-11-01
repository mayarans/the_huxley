while True:
  n = int(input())
  soma = ''
  cont0 = 0
  cont1 = 1
  if n == 0:
    break 
  elif n == 1:
    print('0')
  elif n == 2:
    print('0 1')
  else:
    for i in range (2, n):
      calculo = cont0 + cont1
      soma += f'{calculo} '
      cont0 = cont1
      cont1 = calculo
    print(f'0 1 {soma[0:-1]}')
