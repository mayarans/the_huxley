soma = ''
cont = 0
n = int(input())

for i in range(1, n+1):
  for a in range (1, i+1):
    if i%a==0:
      cont+=1
  if cont > 2:
    soma += f'{i} '
    cont = 0
  else: 
    cont = 0

print(f'1 {soma}')
