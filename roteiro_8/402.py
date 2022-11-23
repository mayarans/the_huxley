def estacaoAno(dia, mes):
    if (dia>=21 and mes==9) or (dia <=20 and mes==12) or (mes>9 and mes<12):
        estacao = 'PRIMAVERA'
    elif (dia>=21 and mes == 12) or (dia<=20 and mes == 3) or (mes>=1 and mes<3):
        estacao = 'VERAO'
    elif (dia>=21 and mes == 3) or (dia<=20 and mes == 6) or (mes>3 and mes<6):
        estacao = 'OUTONO'
    elif (dia>=21 and mes == 6) or (dia<=20 and mes == 9) or (mes>6 and mes<9):
        estacao = 'INVERNO'
    print(estacao)

dia = int(input())
mes = int(input())

estacaoAno(dia, mes)