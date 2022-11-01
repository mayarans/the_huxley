result = ''
cont = 0

while True:
    frase = input()
    if frase == '0':
        break
    else:
        palavras = frase.split()
        for i in range(len(palavras)):
            contLetras = 0
            for a in range(len(palavras[i])):
                contLetras += 1
            if contLetras >= cont:
                maiorPalavra = palavras[i]
                cont = contLetras
            result += f'{contLetras}-'
        print(f'{result[0:-1]}')
        result = ''

print(f'Maior palavra: {maiorPalavra}')           
