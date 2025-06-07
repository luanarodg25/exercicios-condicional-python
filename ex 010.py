custoFab = float(input('Informe o custo de fábrica de um carro: '))

if custoFab > 25000:
    distribuidor = 0.15*custoFab
    imposto = 0.20*custoFab
    preco_consumidor = custoFab + distribuidor + imposto
    print(f'O preço ao consumidor desse carro novo é {preco_consumidor:.2f}')
elif custoFab >= 12000 and custoFab <= 25000:
    distribuidor = 0.10*custoFab
    imposto = 0.15*custoFab
    preco_consumidor = custoFab + distribuidor + imposto
    print(f'O preço ao consumidor desse carro novo é {preco_consumidor:.2f}')
else:
    distribuidor = 0.05*custoFab
    imposto = 0
    preco_consumidor = custoFab + distribuidor + imposto
    print(f'O preço ao consumidor desse carro novo é {preco_consumidor:.2f}')
