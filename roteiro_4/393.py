totalPregos = 0
while True:
  prego = int(input())
  if prego%2!=0:
    break 
  else:
    totalPregos += prego

caixasInteiras = totalPregos//12
if totalPregos%12==0:
  sobra = (caixasInteiras*12) - totalPregos
  valorTotal = 7.89*caixasInteiras
  print(f'{valorTotal:.2f}\n{sobra}')
elif totalPregos%12!=0:
  caixasInteiras +=1
  sobra = (caixasInteiras*12) - totalPregos
  valorTotal = 7.89*caixasInteiras
  print(f'{valorTotal:.2f}\n{sobra}')
