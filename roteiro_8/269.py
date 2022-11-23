def mesPorExtenso(mes):
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    escritaMeses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    if mes in meses:
        for i in range(len(meses)):
            if mes == meses[i]:
                print(f'{escritaMeses[i]}')
    else:
        print('invalido')
            

mes = int(input())
mesPorExtenso(mes)
