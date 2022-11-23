def classificaAluno(media, faltas):
    if media >=9.5 and faltas<=10:
        print('APROVADO COM LOUVOR')
    elif media >=7 and faltas<=10:
        print('APROVADO')
    elif faltas > 10:
        print('REPROVADO POR FALTAS')
    else:
        print('REPROVADO')

media = float(input())
faltas = int(input())
classificaAluno(media, faltas)
