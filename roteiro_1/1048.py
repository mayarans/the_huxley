salario = float(input())
horaExtra = int(input())

valorHora = salario/44
calculoHoraExtra = horaExtra * valorHora
adicional = calculoHoraExtra + calculoHoraExtra * 0.10
salarioFinal = salario + adicional
print(f'{salarioFinal:.2f}')