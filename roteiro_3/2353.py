numerador = 0
peso = 0
semestre = int(input())
if semestre>10 or semestre<=0:
    print('entrada invalida')
else:
    while True:
        ch = int(input())
        nota = int(input())
        tipo = input()
        if (tipo == 'A' or tipo == 'R' or tipo == 'RF') and (ch==33 or ch ==50 or ch == 67 or ch==83):
            x = nota * ch
            numerador+= x
            peso += ch
        semestre = int(input())
        if semestre>10 or semestre<=0:
            break
        

    if peso !=0:
        media = numerador/peso
        print(f'{media:.2f}')
    else:
        print('entrada invalida')
