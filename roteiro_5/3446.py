texto = input()
cont = 0

for i in range(len(texto)):
    if texto[i] == 'a' or texto[i] == 'A':
        cont += 1

print(cont)
