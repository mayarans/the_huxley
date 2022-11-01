x = int(input())
soma = 0

for i in range (1, x): 
  for e in range (1,i+1): 
    if i%e==0:
      soma+=e
  if soma == i*2:
    print(i)
  soma = 0
