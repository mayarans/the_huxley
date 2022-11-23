def listaOrdenada(num):
   numOrdenada = sorted(num)
   print(f'{numOrdenada[2]} eh o maior')

num = list(map(int, input().split()))
listaOrdenada(num)
