ideias, maximo = map(int, input().split()) 
gestos = list(map(int, input().split())) 
resposta = ''

for i in range(len(gestos)):
  for a in range(len(gestos)):
    if i != a:
      calculo = gestos[i] + gestos[a]
      if calculo == maximo:
        resposta = 'SIM'

if resposta == '':
  print('NAO')
else:
  print(resposta)