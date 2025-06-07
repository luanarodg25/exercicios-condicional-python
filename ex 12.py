salario = float(input('Digite o salário de um funcionário: '))
imposto = 0.07 * salario 

if salario <= 350:
    gratificacao = 100
elif salario < 600: 
    gratificacao = 75
elif salario <= 900:
    gratificacao = 50
else:
    gratificacao = 35

salarioFinal = salario + gratificacao - imposto
print(f'O salário a receber desse funcionário é R$ {salarioFinal:.2f}')
