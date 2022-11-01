nome = input()
result = ''
for i in range(len(nome)):
    result += f'{nome.upper()[i]}'
    print(result)
