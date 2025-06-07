preco = float(input('Informe o preço de um produto: '))
codigo = int(input('Informe o código de origem desse produto para saber sua procedência: '))

if codigo == 1:
    procedencia = 'Sul'
    print('Procedência',procedencia)
elif codigo == 2:
    procedencia = 'Norte'
    print('Procedência',procedencia)
elif codigo == 3:
    procedencia = 'Leste'
    print('Procedência',procedencia)
elif codigo == 4:
    procedencia = 'Oeste'
    print('Procedência',procedencia)
elif codigo == 5 or codigo == 6 or (codigo >= 21 and codigo <= 30) :
    procedencia = 'Nordeste'
    print('Procedência',procedencia)
elif codigo == 7 or codigo == 8 or codigo == 9:
    procedencia = 'Sudeste'
    print('Procedência',procedencia)
elif codigo >= 10 and codigo <= 20:
    procedencia = 'Centro-Oeste'
    print('Procedência',procedencia)
else:
    print('Não há procedência para esse código de origem')




