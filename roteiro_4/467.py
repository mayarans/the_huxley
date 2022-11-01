cont = 0
somaPeso = 0
while True:
    peso = float(input())
    cont+=1

    if somaPeso < 560 and cont<=7 and peso>0:
        somaPeso+=peso
    elif peso == 0 or somaPeso >= 560 or cont > 7:
        break
        

print(f'{cont-1}')
print(f'{somaPeso:.1f}')
