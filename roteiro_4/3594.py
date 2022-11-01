cont = 0
primo = 0
n1 = int(input())
n2 = 0
while n2 <= n1:
  n2 = int(input())
  if n2 <= n1:
    print('Digite um valor maior que o primeiro!')

for i in range (n1, n2+1):
  for a in range(1, i+1):
    if i%a==0:
      cont+=1
  if cont ==2:
    primo+=i
    cont = 0
  else:
    cont = 0

if primo == 0:
  print('Sem numeros primos no intervalo informado.')
else:
  print(primo)
