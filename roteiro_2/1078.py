nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

media = (nota1 + nota2 + nota3)/3

if nota1 >= 0 and nota2>= 0 and nota3>= 0:
    if media >= 70:
        print(f'A media do aluno foi {media:.2f} e ele foi APROVADO')
    elif media >= 40:
        print(f'A media do aluno foi {media:.2f} e ele foi FINAL')
    elif media >= 0:
        print(f'A media do aluno foi {media:.2f} e ele foi REPROVADO')
else:
    print('Media invalida')
