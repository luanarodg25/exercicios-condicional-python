idade = int(input('Digite a idade de uma pessoa: '))
peso = float(input('Digite o peso de uma pessoa: '))

if idade < 20:
    if peso < 60:
        risco= 9
    elif peso <= 90:
        risco = 8
    else:
        risco = 7
elif idade >= 20 and idade <= 50:
    if peso < 60:
        risco= 6
    elif peso <= 90:
        risco = 5
    else:
        risco = 4
else:
    if peso < 60:
        risco= 3
    elif peso <= 90:
        risco = 2
    else:
        risco = 1

print('O grupo de risco que essa pessoa se encaixa é: ',risco)

