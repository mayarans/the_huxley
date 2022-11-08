bandejas = int(input())
quebrou = 0

for i in range(bandejas):
  latas, copos = map(int, input().split())
  if latas > copos: 
    quebrou += copos

print(quebrou)
