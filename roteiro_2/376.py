livros = int(input())
alunos = int(input())
avaliacao = alunos / livros

if avaliacao <= 8: 
    print('A')
elif avaliacao <= 12 and avaliacao >= 9:
    print('B')
elif avaliacao <= 18 and avaliacao >= 13:
    print('C')
elif avaliacao > 18:
    print('D')
