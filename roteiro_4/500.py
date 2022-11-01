n1 = int(input())
n2 = int(input())
cont = 0
soma = ''
if n1>n2:
  for i in range (n1, n2-1, -1):
    for a in range (1, i+1):
      if i%a==0:
        cont+=1
    if cont == 2:
      soma += f'{i}\n'
      cont = 0
    else:
      cont = 0

  print(soma[0:-1])
else:
  for i in range (n2, n1-1, -1):
    for a in range (1, i+1):
      if i%a==0:
        cont+=1
    if cont == 2:
      soma += f'{i}\n'
      cont = 0
    else:
      cont = 0

  print(soma[0:-1])
