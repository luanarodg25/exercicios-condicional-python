numero1 = int(input('Informe o 1° número: '))
numero2 = int(input('Informe o 2° número: '))
numero3 = int(input('Informe o 3° número: '))

if numero1 == numero2 == numero3:
    print('Todos os números são iguais')  
elif numero1 >= numero2 and numero1 >= numero3:
    print(numero1, 'é o maior')           
elif numero2 >= numero1 and numero2 >= numero3:
    print(numero2, 'é o maior')           
else:
    print(numero3, 'é o maior')           
