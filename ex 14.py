salario = float(input('Informe o salário de um funcionário: '))

if salario <= 300:
    aumento = 0.50
elif salario <= 500:
    aumento = 0.40
elif salario <= 700:
    aumento = 0.30
elif salario <= 800:
    aumento = 0.20
elif salario <= 1000:
    aumento = 0.10
else:
    aumento = 0.05
aumento = salario * aumento
novoSalario = salario + aumento
print(f'O novo salário desse funcionário é {novoSalario:.2f}')
