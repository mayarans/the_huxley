entrada = input()

while entrada != 'FIM':
    entrada = entrada.split()
    l1 = int(entrada[0])
    l2 = int(entrada[1])
    l3 = int(entrada[2])

    if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l1+l2):
        if l1 == l2 == l3:
            print('EQUILATERO')
        elif l1!= l2 and l1 !=l3 and l2!=l3:
            print('ESCALENO')
        elif l1 == l2 and l1!=l3:
            print('ISOSCELES')
        elif l2 == l3 and l2!=l1:
            print('ISOSCELES')
        elif l1 == l3 and l1!=l2:
            print('ISOSCELES')
    else:
        print('INVALIDO')
    entrada = input()
