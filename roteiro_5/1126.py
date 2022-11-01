frase = input()
palavras = frase.split()
mensagem = ''

for i in range(len(palavras)):
    result = ''
    if i%2 != 0:
        for a in palavras[i][::-1]:
            result += a
        mensagem += f'{result} '
    else:
        mensagem += f'{palavras[i]} '
print(mensagem)
