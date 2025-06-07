altura = float(input('Informe a altura de uma pessoa em metros: '))
sexo = input('Informe o sexo de uma pessoa: ').upper()

if sexo == 'F':
    pesoideal = (62.1*altura)-58
    print(f'O peso ideal dessa pessoa é {pesoideal:.2f} kg')
elif sexo == 'M':
    pesoideal = (72.7*altura)-44.7
    print(f'O peso ideal dessa pessoa é {pesoideal:.2f} kg')
else:
    print('Sexo inválido. Digite M para masculino e F para feminino') 
                     
