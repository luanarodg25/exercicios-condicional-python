print('-MENU DE OPÇÕES-')
print('Tipo  Descrição          Rendimento Mensal')
print('1->   Poupança                  3%')
print('2-> Poupança de renda fixa      4%')
print()

valor = float(input('Valor do investimento: '))
escolha = int(input('Escolha uma opção: '))

if escolha == 1:
    rendimento = 0.03
    resultado = valor * rendimento
    valorF = valor + resultado
    print(f'O valor corrigido apos um mês de investimento é {valorF:.2f}')
elif escolha == 2:
    rendimento = 0.04
    resultado = valor * rendimento
    valorF = valor + resultado
    print(f'O valor corrigido apos um mês de investimento é {valorF:.2f}')
else:
    print('Escolha inválida, escolha o tipo 1 ou 2')


