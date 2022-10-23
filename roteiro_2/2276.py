psnr = int(input())
enquadramento = input()
exposicao = input()

if psnr < 50 and enquadramento == 'excelente' and exposicao == 'bem exposta':
  print('marromeno')
elif psnr >= 80 and psnr <=90:
  if enquadramento == 'bom' or enquadramento == 'excelente':
    if exposicao == 'bem exposta':
      print('para imprimir')
    elif exposicao == 'subexposta' or exposicao == 'superexposta':
      print('boa')
    else:
      print('marromeno')
  else:
    print('marromeno')
elif psnr >= 50 and psnr <= 80:
  if enquadramento == 'excelente' and exposicao == 'bem exposta':
    print('boa')
  else:
    print('marromeno')
else:
  print('lixo')
