valor = 1
cont = 0
valores = 0

while valor != 0:
  valor = int(input())
  if valor !=0:
    cont +=1
  valores += valor 
  

media = valores / cont
if media < 110:
  print('Glicose Normal')
elif media >= 200:
  print('Glicose Muito Alta')
else:
  print('Glicose Alterada')
