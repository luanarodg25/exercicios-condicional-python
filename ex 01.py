nota1 = float(input('Informe a primeira nota de um aluno: '))
nota2 = float(input('Informe a segunda nota de um aluno: '))
nota3 = float(input('Informe a terceira nota de um aluno: '))
nota4 = float(input('Informe a quarta nota de um aluno: '))

media = (nota1+nota2+nota3+nota4)/4
if media >= 7:
    print('O aluno está aprovado')
else:
    print('O aluno está reprovado')
