interface = int(input('Trabalho aborda Interface Grafica? (0 - Nao 1 - Sim)'))
print()
intArtificial = int(input('Trabalho aborda Inteligencia Artificial? (0 - Nao 1 - Sim)'))
print()
encaps = int(input('Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)'))
print()
identacao = int(input('Trabalho aborda Indentacao? (0 - Nao 1 - Sim)'))
print()
structs = int(input('Trabalho aborda Structs? (0 - Nao 1 - Sim)'))
print()
if interface == 1 or intArtificial == 1:
    if encaps == 1 and identacao == 1:
        if structs == 1:
            print('Seu trabalho sera avaliado.')
        else:
            print('Seu trabalho nao sera avaliado, nota 0.')
    else: 
        print('Seu trabalho nao sera avaliado, nota 0.')
else:
    print('Seu trabalho nao sera avaliado, nota 0.')
       
    