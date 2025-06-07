codigo = int(input('Informe o código do produto: '))
quantidade = int(input('Informe a quantidade comprada desse produto: '))

if 1 <= codigo <= 10:
    preco_unitario = 10
elif 11 <= codigo <= 20:
    preco_unitario = 15
elif 21 <= codigo <= 30:
    preco_unitario = 20
elif 31 <= codigo <= 40:
    preco_unitario = 30
else:
    print('Código inválido!')
    exit()

preco_total = quantidade * preco_unitario

if preco_total <= 250:
    desconto = preco_total * 0.05
elif preco_total <= 500:
    desconto = preco_total * 0.10
else:
    desconto = preco_total * 0.15

preco_final = preco_total - desconto

print(f'\nPreço unitário do produto: R$ {preco_unitario:.2f}')
print(f'Preço total da nota: R$ {preco_total:.2f}')
print(f'Valor do desconto: R$ {desconto:.2f}')
print(f'Preço final da nota: R$ {preco_final:.2f}')

