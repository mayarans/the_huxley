n = int(input())

for i in range(n):
    palavra = input()
    semEspaco = palavra.replace(' ', '')
    if semEspaco.upper() == semEspaco.upper()[::-1]:
        print('SIM')
    else:
        print('NAO')