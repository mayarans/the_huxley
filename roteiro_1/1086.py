dias = int(input())
quilometros = int(input())
calculo = dias * 30 + 0.01 * quilometros
total = calculo - (calculo * 0.10)
print(f'{total:.2f}')