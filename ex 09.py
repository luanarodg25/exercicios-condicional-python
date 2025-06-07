saldoMedio = float(input('Informe o saldo médio de um cliente: '))
print()
if saldoMedio > 400:
    percentual = 0.30
elif saldoMedio > 300:
    percentual = 0.25
elif saldoMedio > 200:
    percentual = 0.20
else:
    percentual = 0.10

credito = saldoMedio * percentual
print(f'O saldo médio é {saldoMedio}')
print(f'O valor do crédito é R${credito:.2f}')
