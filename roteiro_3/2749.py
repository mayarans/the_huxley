l = 1
r = 1
while l != 0 and r != 0:
    entrada = input().split()
    l = int(entrada[0])
    r = int(entrada[1])
    if l == 0 and r == 0:
        print()
    else:   
        soma = l + r
        print(soma)
