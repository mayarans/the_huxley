nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

if nota1>=nota2 and nota1>=nota3:
  if nota2>nota3:
    print(f'{nota3}\n{nota2}\n{nota1}')
  elif nota3>nota2:
    print(f'{nota2}\n{nota3}\n{nota1}')
  elif nota3==nota2:
    print(f'{nota2}\n{nota3}\n{nota1}')
elif nota2>=nota1 and nota2>=nota3:
  if nota1>nota3:
    print(f'{nota3}\n{nota1}\n{nota2}')
  elif nota3>nota1:
    print(f'{nota1}\n{nota3}\n{nota2}')
  elif nota3==nota1:
    print(f'{nota1}\n{nota3}\n{nota2}')
elif nota3>=nota1 and nota3>=nota2:
  if nota1>nota2:
    print(f'{nota2}\n{nota1}\n{nota3}')
  elif nota2>nota1:
    print(f'{nota1}\n{nota2}\n{nota3}')
  elif nota2==nota1:
    print(f'{nota1}\n{nota2}\n{nota3}')
elif nota1==nota2==nota3:
  print(f'{nota1}\n{nota2}\n{nota3}')
