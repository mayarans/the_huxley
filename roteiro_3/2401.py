k = int(input())
i = int(input())
m = int(input())
n = int(input())
d = int(input())

cont = 0
while d > 0:
    if d % k == 0 or d%i==0 or d%m==0 or d%n == 0:
        cont+=1
    d = d - 1

print(cont)
