def volumeEsfera(raio):
    volume = (raio**3*3.1416*4)/3
    print(f'{volume:.2f}')

for i in range(3):
    raio = float(input())
    volumeEsfera(raio)