listaNum = []
for i in range(27):
    listaNum.append(i)

listaAlpha = ' abcdefghijklmnopqrstuvwxyz'

while True:
    n = input().split() 
   
    if n == ['6', '9', '13']:
        break
    else:
        frase = ''
        for i in n:
            frase += f'{listaAlpha[int(i)]}'
        print(frase)
