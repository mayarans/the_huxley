cont = 0

while True:
  port = int(input())
  if port < 0:
    break 
  else:
    mat = int(input())
    red = float(input())
    if port >= (0.8*50) and mat >= (0.6*35) and red >= 7:
      cont += 1

print(cont)
