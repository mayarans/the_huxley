soma_peso = 0
qtd_livros = 0
while True:
  peso_livro = int(input())
  if soma_peso + peso_livro <= 18:
    soma_peso += peso_livro
    qtd_livros += 1
  else:
    print(qtd_livros)
    break