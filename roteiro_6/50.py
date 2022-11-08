h1 = float(input())
h2 = float(input())
h3 = float(input())
h4 = float(input())

alturas = [h1, h2, h3, h4]
ordem = sorted(alturas)

print(f'{ordem[0]:.2f}\n{ordem[2]:.2f}\n{ordem[3]:.2f}\n{ordem[1]:.2f}')