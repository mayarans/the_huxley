raio = float(input())
angulo = float(input())
pi = 3.14
comprimento = (pi * raio * angulo)/180
area = pi * raio ** 2 * (angulo/360)
print(f'{comprimento:.2f}\n{area:.2f}')