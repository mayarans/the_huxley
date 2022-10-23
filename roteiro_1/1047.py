nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

peso1 = int(input())
peso2 = int(input())
peso3 = int(input())

a = (nota1 + nota2 + nota3) / 3
p = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
h = 3 / (1/nota1 + 1/nota2 + 1/nota3)

print(f'a: {a:.1f}\np: {p:.1f}\nh: {h:.1f}')