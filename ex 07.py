salario = float(input('Informe o valor do salário de um funcionário: '))

if salario <= 500:
    aumento = (30/100)*salario
    salarioF = salario + aumento
    print(f'O salário reajustado desse funcionário é {salarioF}')
else:
    print('O funcionário não possui direito ao aumento, pois seu salário é maior que 500 reais')
