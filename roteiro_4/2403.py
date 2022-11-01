x = int(input())
cont = 0
y = x
maiorCont = 0
divisor = 0

for i in range (2, x+1):
  if cont>maiorCont:
    divisor = i-1
    maiorCont = cont
    print(f'este é o maior contador {maiorCont}')
    cont = 0
  else:
    cont = 0
  while True:
    if y%i==0:
      cont+=1
      print(f'o contador agora vale {cont}')
      y = y/i
      print(f'novo valor de y: {y}')
    else:
      y = x
      break
  
print(f'mostFrequent: {divisor}, frequency: {maiorCont}')
