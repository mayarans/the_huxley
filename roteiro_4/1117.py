maior_velocidade = 0
maior_ano = 0
total_velocidade = 0
qtd_carros = 0

while True:
  entrada = input()
  if entrada == 'n' or entrada == 'N':
    break
  ano = int(input())
  velocidade = float(input())
  total_velocidade += velocidade
  qtd_carros += 1

  if ano > maior_ano:
    maior_ano = ano
  if velocidade > maior_velocidade:
    maior_velocidade = velocidade

if maior_ano == 0:
  print("zero")
else:
  print(f"{maior_velocidade:.2f}")
  print(maior_ano)
  print(f"{(total_velocidade / qtd_carros):.2f}")
