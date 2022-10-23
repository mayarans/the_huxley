tipo = input()
if tipo == 'a' or tipo == 'p' or tipo == 'h':
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())

    if tipo == 'a':
        a = (nota1 + nota2 + nota3) / 3
        if a >= 70:
            print(f'{a:.2f}\nAprovado')
        elif a >= 40:
            print(f'{a:.2f}\nFinal')
        elif a >= 0:
            print(f'{a:.2f}\nReprovado')
    elif tipo == 'p':
        peso1 = int(input())
        peso2 = int(input())
        peso3 = int(input())
        p = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
        if p >= 70:
            print(f'{p:.2f}\nAprovado')
        elif p >= 40:
            print(f'{p:.2f}\nFinal')
        elif p >= 0:
            print(f'{p:.2f}\nReprovado')
    elif tipo == 'h':
        h = 3 / (1/nota1 + 1/nota2 + 1/nota3)
        if h >= 70:
            print(f'{h:.2f}\nAprovado')
        elif h >= 40:
            print(f'{h:.2f}\nFinal')
        elif h >= 0:
            print(f'{h:.2f}\nReprovado')
else: 
    print('Escolha um tipo de media valida.')
