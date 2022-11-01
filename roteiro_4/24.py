fatorial = 1
while True:
  n = int(input())
  if n == -1:
    break 
  else:
    for i in range(n, 0, -1):
      fatorial *= i
    print(fatorial)
    fatorial = 1
