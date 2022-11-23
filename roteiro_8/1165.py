def verificarTexto(texto):
  temNumero = 0
  if texto == '':
    print('vazio\n0')
  else:
    for i in texto:
      if i.isnumeric():
        temNumero +=1
    if temNumero == 0:
      codificacao(texto)
    else:
      print('numeros\n0')

def codificacao(texto):
  cont = 0
  contVerificar = 0
  resultado = ''
  simbolos = ['@', 3, 1, 0, 7, 5]
  letras = ['A', 'E', 'I', 'O', 'T', 'S']
  for i in texto[::-1]:
    contVerificar = 0
    for a in letras:
      if i == a:
        cont += 1
        contVerificar += 1
        resultado += f'{simbolos[letras.index(a)]}'
    if contVerificar == 0:
      resultado += f'{i}'
  print(f'{resultado.lower()}\n{cont}')


texto = input().upper()
verificarTexto(texto)
    
