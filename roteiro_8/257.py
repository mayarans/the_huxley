def ehNumero(frase):
    cont = 0
    for i in frase:
        if i.isnumeric():
            cont+=1
    print(cont)

frase = input()
ehNumero(frase)