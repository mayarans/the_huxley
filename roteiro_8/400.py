def calculaMulta(x):
    multa = 0
    if x>50:
        excedeu = x - 50
        if excedeu <= 0.1*x:
            multa = 230
        elif excedeu <= 0.2*x:
            multa = 340
        else:
            multa = excedeu*19.28

    print(f'{multa:.2f}')

velocidade = int(input())
calculaMulta(velocidade)