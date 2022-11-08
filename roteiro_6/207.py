competidores, voltas = map(int, input().split())
menorTempo = 1000000000000

for i in range(competidores):
    tempo = list(map(int, input().split()))
    if sum(tempo) < menorTempo:
        ganhador = f'{i+1}'
        menorTempo = sum(tempo)

print(ganhador)