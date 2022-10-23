a = int(input())

if a >= 18:
  b = input()
  c = input()
  d = input()
  e = int(input())
  f = input()
  g = input()
  h = input()
  if b == 'N':
    if c == 'S' and d == 'S':
      if (a - e) >= 16:
        if f == 'S':
            if e >= 12 and h == 'S':
                print('Pode adotar')
            elif e < 12 and h == 'N':
              print('Pode adotar')
            else:
              print('Não pode adotar')
        elif f == 'N':
          if g == 'S':
            if e >= 12 and h == 'S':
              print('Pode adotar')
            elif e < 12 and h == 'N':
              print('Pode adotar')
            else:
              print('Não pode adotar')
          else: 
            print('Não pode adotar')
        else:
          print('Não pode adotar')
      else:
        print('Não pode adotar')
    elif c == 'N' and d == 'N':
      if (a - e) >= 16:
        if f == 'S':
          if g == 'S':
            if e >= 12 and h == 'S':
                print('Pode adotar')
            elif e <12 and h == 'N':
              print('Pode adotar')
            else:
              print('Não pode adotar')
          else:
            print('Não pode adotar')
        elif f == 'N':
          if g == 'S':
            if e>=12 and h == 'S':
              print('Pode adotar')
            elif e < 12 and h == 'N':
              print('Pode adotar')
            else:
              print('Não pode adotar')
          else:
           print('Não pode adotar')
        else:
          print('Não pode adotar')
      else:
        print('Não pode adotar')
    else:
      print('Não pode adotar')
  else:
    print('Não pode adotar')
else:
  print('Não pode adotar')
  