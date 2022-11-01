soma1 = 0
for i in range(5):
    soma = 0
    n = int(input())
    for a in range(1, n+1):
        if n%a==0:
            soma+=a
    if soma>soma1:
        x = f'{n}' 
        soma1 = soma
print(x)
