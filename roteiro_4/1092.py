mulher = 0
homem = 0
salarioMulher = 0
salarioHomem = 0
salarioMaior = 0


for i in range(10):
  salario = float(input())
  sexo = input()
  if salario > salarioMaior:
    maior = sexo
    salarioMaior = salario
  if sexo == 'm':
    homem+=1
    salarioHomem += salario
  elif sexo == 'f':
    mulher+=1
    salarioMulher += salario

mediaTotal = (salarioHomem+salarioMulher)/(homem+mulher)
mediaHomem = salarioHomem / homem 

print(f'{homem}\n{mulher}\n{mediaTotal:.1f}\n{maior}\n{mediaHomem:.1f}')
