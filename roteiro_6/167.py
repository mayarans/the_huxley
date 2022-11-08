contBranco = 0
contNulo = 0
contValidos = 0
contAlibaba = 0
contAlcapone = 0

while True:
    n = int(input())
    if n == -1:
        break 
    elif n == 0:
        contBranco +=1
    elif n == 83:
        contValidos += 1
        contAlibaba += 1
    elif n == 93:
        contValidos +=1
        contAlcapone += 1
    else:
        contNulo +=1

percentAlibaba = (contAlibaba*100)/(contValidos + contBranco)
percentAlcapone = (contAlcapone*100)/(contValidos + contBranco)

if contAlcapone > contAlibaba:
    vencedor = '93'
else:
    vencedor = '83'

print(f'{contAlibaba}\n{contAlcapone}\n{contBranco}\n{contNulo}\n{vencedor}\n{percentAlibaba:.2f}\n{percentAlcapone:.2f}')
