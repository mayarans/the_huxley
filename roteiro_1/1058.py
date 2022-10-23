temperaturaDoGas = float(input()) 
massaMolar = float(input())
constante = 8.31
velocidade = ((3 * constante * temperaturaDoGas) / massaMolar) ** (1/2)
print(f'{velocidade:.2f}')