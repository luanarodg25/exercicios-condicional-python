print('MENU DE OPÇÕES')
print('Categoria: 1 - Limpeza | 2 - Alimentação | 3 - Vestuário')
print('Situação: R - Produtos que necessitam de refrigeração | N - Produtos que não necessitam de refrigeração')
print()
preco = float(input('Informe o preço de um produto: '))
categoria = int(input('Informe a categoria: '))
if categoria != 1 and categoria != 2 and categoria != 3:
    print('Categoria inválida, digite 1,2 ou 3 para as categorias conforme o menu')
    exit()
situacao = input('Informe a situação: ').upper()
if situacao != 'R' and situacao != 'N':
    print('Situação inválida, digite R ou N para as categorias conforme o menu')
    exit()
print()

if preco <= 25:
    if categoria == 1:
        aumento = 0.05
    elif categoria == 2:
        aumento = 0.08
    elif categoria == 3:
        aumento = 0.10
elif preco > 25:
    if categoria == 1:
        aumento = 0.12
    elif categoria == 2:
        aumento = 0.15
    elif categoria == 3:
        aumento = 0.18
        
if categoria == 2 or situacao == 'R':
    imposto = 0.05*preco
else:
    imposto = 0.08*preco

valor_aumento = preco * aumento
valor_imposto = imposto
novo_preco = preco + valor_aumento - valor_imposto

if novo_preco <= 50:
    classificacao = 'Barato'
elif novo_preco > 50 and novo_preco < 120:
    classificacao = 'Normal'
else:
    classificacao = 'Caro'

print(f'O valor do aumento: {valor_aumento:.2f}')
print(f'O valor do imposto: {valor_imposto:.2f}')
print(f'O novo preço: {novo_preco:.2f}')
print(f'A classificação desse produto é {classificacao}')



