dias= 0
cont = 0
valorInicial = float(input()) 
soma = valorInicial

while dias < 6:
    dias += 1
    valor = float(input()) 
    soma+=valor
    if valor >= valorInicial+0.5:
        cont+=1
    valorInicial = valor
    

print(f'R$ {soma:.2f}\n{cont}')
