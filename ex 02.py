nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2
print(media)
if media >= 0 and media < 3:
    print('Reprovado')
elif media >= 3 and media < 7:
    print('Exame')
elif media >= 7 and media <=10:
    print('Aprovado')
