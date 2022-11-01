numeros_negativos = 0
for i in range(5):
  A = float(input("Digite um valor:\n"))
  if A < 0:
    numeros_negativos += 1
print(f"Foram digitados {numeros_negativos} numeros negativos")