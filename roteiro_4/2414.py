cubos = int(input())
nivel = 0
cont = 0
altura = 0
soma = 0

while cubos > soma:
  cont+=1
  nivel+=1*cont
  soma+= nivel
  if soma > cubos:
    break
  altura += 1

print(altura)
