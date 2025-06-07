idade = int(input('Informe a idade de um nadador para saber sua categoria: '))

if idade < 5:
    print('Não há categoria')
elif idade >= 5 and idade <=7:
    print('Infantil')
elif idade >= 8 and idade <=10:
    print('Juvenil')
elif idade >= 11 and idade <=15:
    print('Adolescente')
elif idade >= 16 and idade <=30:
    print('Adulto')
else:
    print('Sênior')
    
