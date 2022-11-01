N = int(input())
P = int(input())
S = 0
for i in range(N):
  X = int(input())
  Y = int(input())
  if X + Y >= P and X != 0 and Y != 0:
    S += 1
print(S)