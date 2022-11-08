n = int(input())
if n > 0:
  notas = []

  for i in range(n):
    nota = float(input())
    notas.append(nota)

  for i in range(len(notas)):
    print(f'Nota {i+1}: {notas[i]}')

  media = sum(notas)/n
  print(f'Media: {media:.2f}')
else:
  print('Numero de notas invalido.')