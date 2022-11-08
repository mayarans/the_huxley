tipo = int(input())
resposta = list(map(int, input().split()))
cont = 0

for i in resposta:
    if i == tipo:
        cont+=1

print(cont)