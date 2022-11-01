N = int(input())
M = int(input())
if N > M:
  M, N = N, M
S = 0

for i in range(N, M + 1):
  if i > 0:
    S += i
print(S)