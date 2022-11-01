maiorMedia = 0
calculo = 0
while True:
    media = int(input(''))
    if media ==0:
        break
    elif media >100 or media<0:
        continue
    else:
        nome = input('')
        horas = int(input(''))
        if media < 70:
            print('Aluno NAO pode concorrer.')
            continue
        elif horas >=8:
            cre = int(input(''))
            prova = -1
            while prova <0 or prova >100:
                prova = int(input(''))
            calculo = (media * 0.4) + (cre * 0.1) + (prova * 0.5) / (0.4+0.1+0.5)
            if prova <70:
                print('Aluno reprovado na prova de monitoria!')
            elif prova>=70 and calculo >=70:
                print(f'Aluno aprovado! Sua media foi {calculo:.2f}.')
            elif prova>=70 and calculo<70:
                print(f'Aluno reprovado na selecao. Media= {calculo:.2f}.')
        else:
            print('Aluno NAO pode concorrer.')
    if calculo>maiorMedia:
        resposta = f'Resultado da monitoria: {nome}, {calculo:.2f}.'
        maiorMedia = calculo

if maiorMedia>=70:
    print(resposta)
else: 
    print('Resultado da monitoria: Sem alunos aprovados.')

