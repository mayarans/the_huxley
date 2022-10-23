vogal = input()

vogais = 'aeiouAEIOU'

if len(vogal) == 1 and vogal in vogais:
  print('Eh vogal')
elif len(vogal) == 1 and vogal not in vogais:
  print('Nao eh vogal')
else: 
  print('1 caractere, por favor!')
