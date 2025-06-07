preco = float(input('Informe o preço de um produto: '))

if preco <= 50:
    aumento = 0.05
elif preco <= 100:
    aumento = 0.10
else:
    aumento = 0.15

novoP = preco + (aumento*preco)

if novoP <= 80:
    classificacao = 'Barato'
elif novoP <= 120:
    classificacao = 'Normal'
elif novoP <= 200:
    classificacao = 'Caro'
else:
    classificacao = 'Muito caro'

print(f'O novo preço desse produto é {novoP:.2f}')
print(f'Sua classificação é: {classificacao}')
