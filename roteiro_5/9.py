while True:
    result = ''
    n = int(input())
    if n == 0:
        break 
    else:
        palavra = input()
        for i in range(n, 0, -1):
            result += f'{palavra[i-1]}'
        print(result)
