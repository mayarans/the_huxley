raio1 = float(input())
raio2 = float(input())
pi = 3.14

area1 = pi * raio1 **2
area2 = area = pi * raio2 **2

if area1 > area2:
    print('Primeiro circulo')
elif area2 > area1: 
    print('Segundo circulo')
else: 
    print('Iguais')
