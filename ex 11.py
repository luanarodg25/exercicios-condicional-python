salario = float(input('Informe o salário de um funcionário: '))

if salario <= 300:
    aumento = 0.15*salario
    novoSalario = salario + aumento
    print(f'O aumento no salário desse funcionário é {aumento}')
    print(f'O novo salário desse funcionário é {novoSalario:.2f}')

elif salario > 300 and salario < 600:
    aumento = 0.10*salario
    novoSalario = salario + aumento
    print(f'O aumento no salário desse funcionário é {aumento}')
    print(f'O novo salário desse funcionário é {novoSalario:.2f}')

elif salario >= 600 and salario <= 900:
    aumento = 0.05*salario
    novoSalario = salario + aumento
    print(f'O aumento no salário desse funcionário é {aumento}')
    print(f'O novo salário desse funcionário é {novoSalario:.2f}')

else:
    aumento = 0
    novoSalario = salario
    print('Ele não teve aumento pois seu salário é superior a 900,00')
    print(f'O salário desse funcionário é {novoSalario:.2f}')
