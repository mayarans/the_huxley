while True:
  cont = 0
  n = int(input())
  if n == -1:
    break 
  else:
    for i in range (1, n+1):
      if n%i==0:
        cont+=1
  if cont == 2:
    print(1)
  else:
    print(0)
