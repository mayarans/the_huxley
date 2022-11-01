N = int(input())
S = 0
for i in range(1, N + 1):
  if i > 1:
    print(" + ", end="")
  print(f"{i}/{i * 3}", end="")
  S += i / (i * 3)
print(("\n" if S > 0 else "") + f"{S:.2f}")