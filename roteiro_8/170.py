def ehPrimo(num):
    numEhPrimo = 0
    for i in num:
        contPrimo = 0
        for a in range(1, i+1):
            if i%a==0:
                contPrimo+=1
        if contPrimo == 2:
            numEhPrimo +=1
    return numEhPrimo
    

num = list(map(int, input().split()))

if ehPrimo(num) == 4:
    resultado = 1
    for i in range(4):
        resultado *= num[i]
    print(resultado)
else:
    print('SEM PRODUTO')