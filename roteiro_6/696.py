lista = []
cont = 0
for i in range(10):
  numero = int(input())
  lista.append(numero)

x = int(input())

for i in range(len(lista)):
  if lista[i] == x:
    cont+=1
  
print(cont)