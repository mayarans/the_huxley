soma_cre = 0
qtd_cre = 0
menor_cre = 1000
matricula_menor_cre = 0

while True:
  matricula = input()
  if matricula == "999": break
  cre = float(input())

  soma_cre += cre
  qtd_cre += 1

  if cre < menor_cre:
    menor_cre = cre
    matricula_menor_cre = matricula

print(matricula_menor_cre)
print(f"{(soma_cre / qtd_cre):.2f}")
