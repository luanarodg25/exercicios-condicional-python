preco = float(input('Informe o preço atual de um produto: '))
codigo = int(input('Código do produto: '))

if preco <= 30:
    desconto = 'Sem desconto'
    novoP = preco
    print(f'{desconto}')
    print(f'O novo preço do produto foi R${novoP:.2f}')

elif preco < 100:
    desconto = 0.10*preco
    novoP = preco - desconto
    print(f'O desconto foi de R${desconto:.2f}')
    print(f'O novo preço do produto foi R${novoP:.2f}')

else:
    desconto = 0.15*preco
    novoP = preco - desconto
    print(f'O desconto foi de R${desconto:.2f}')
    print(f'O novo preço do produto foi R${novoP:.2f}')



