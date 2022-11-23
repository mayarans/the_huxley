def contagemRegressiva(n):
    for i in range(n, 0, -1):
        resultado = ''
        for a in range(i):
            resultado += f'{i}-'
        print(resultado[0:-1])
        
n = int(input())
contagemRegressiva(n)