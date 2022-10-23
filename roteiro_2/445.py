dias = int(input())
quilometragemTotal = int(input())
calculo = quilometragemTotal - (100*dias)

if dias == 1 and calculo <= 0:
    diaria = 90
    print(f'{diaria:.2f}')
elif dias == 1 and calculo > 0:
    extra = calculo * 12
    total = 90 + extra
    print(f'{total:.2f}')
elif dias > 1 and calculo <= 0:
    diaria = 90 * dias
    print(f'{diaria:.2f}')
elif dias > 1 and calculo > 0:
    diaria1 = 90 * dias 
    extra = calculo * 12
    total = diaria1 + extra 
    print(f'{total:.2f}')