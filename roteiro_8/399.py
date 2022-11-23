def calculaHospedagem(tipo, quantDiaria):
  valor = 0
  if tipo == 'INDIVIDUAL':
    valor = quantDiaria*125
  elif tipo == 'SUÍTE DUPLA':
    valor = quantDiaria*140
  elif tipo == 'SUÍTE TRIPLA':
    valor = quantDiaria*180
  if quantDiaria >= 3:
    valorTotal = valor -  valor*0.15
    valor = valorTotal
  return valor

tipo = input().upper()
dias = int(input())
print(f'{calculaHospedagem(tipo, dias):.2f}')