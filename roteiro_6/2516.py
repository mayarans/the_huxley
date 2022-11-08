n = int(input())
x = sorted(list(map(int, input().split())))

if n % 2 != 0:
  encontro = x[int(n/2)]
else:
  encontro = x[int((n/2)-1)]
  
diferenca = 0

for i in range(n):
    diferenca += abs(x[i]-encontro)

print(f'{diferenca} {encontro}')
