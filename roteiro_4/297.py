anos = input().split()
anoi = int(anos[0])
anof = int(anos[1])
cont = 0

for i in range(anoi, anof+1):
    if (i%4==0 and i%100!=0) or (i%4==0 and i%100==0 and i%400==0):
        print(i)
        cont+=1

if cont == 0:
    print(-1)