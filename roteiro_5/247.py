palavra = input()
result = ''
for i in range(len(palavra), 0, -1):
    result += palavra[i-1]
print(result)