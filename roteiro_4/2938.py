agora = 0
depois = 0
while True:
  doacao = int(input(''))
  if doacao <1:
    break
  else:
    opcao = 0
    while opcao != 1 and opcao !=2:
      opcao = int(input(''))
      if opcao != 1 and opcao != 2:
        print('Valor invalido')
      elif opcao == 2:
        meses = 0
        while meses < 2 or meses > 12:
          meses = int(input())
          if meses < 2 or meses > 12:
            print('Favor digitar valor entre 2 e 12, inclusive')
          else:
            agora+=doacao
            calculo = doacao*(meses-1)
            depois+=calculo
      elif opcao ==1:
        agora+=doacao

print(f'Total arrecadado para agora: R$ {agora:.2f}\nTotal arrecadado para meses futuros: R$ {depois:.2f}')
