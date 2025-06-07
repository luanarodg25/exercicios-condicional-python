salario = float(input('Digite o salário de um funcionário: '))

if salario <= 300:
    aumento = (35/100)*salario
    salarioF = salario + aumento
    print(f'Com o aumento de 35% o salário final desse funcionário é {salarioF:.2f}')
else:
    aumento = (15/100)*salario
    salarioF = salario + aumento
    print(f'Com o aumento de 15% o salário final desse funcionário é {salarioF:.2f}')
