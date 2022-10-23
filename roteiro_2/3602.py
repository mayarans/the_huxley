t1 = int(input())
t2 = int(input())
t3 = int(input())
t4 = int(input())

if 2<= t1 <= 6 and 2<= t2 <= 6 and 2<= t3 <= 6 and 2<= t4 <= 6:
  x = (t1-1) + (t2-1) + (t3-1) + t4
  print(x)
else:
  print('Requisito violado')
