n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print("====== MENU ======")
print("1 -> Média entre os números digitados")
print("2 -> Diferença do maior pelo menor")
print("3 -> Produto entre os números digitados")
print("4 -> Divisão do primeiro pelo segundo")
print()
escolha = int(input('Informe a opção desejada: '))
print()
if escolha == 1:
    media = (n1+n2)/2
    print('A média entre os números é',media)
elif escolha == 2:
    if n1 > n2:
        diferenca = n1 - n2
        print('A diferença de',n1,'por',n2,'é',diferenca)
    elif n2 > n1:
        diferenca = n2 - n1
        print('A diferença de',n2,'por',n1,'é',diferenca)
    else:
        print('Os números digitados são iguais, portanto a diferença é 0')
elif escolha == 3:
    produto = n1 * n2
    print('O produto entre os números é',produto)
elif escolha == 4:
    if n2 == 0:
        print('A divisão não pode ser realizada pois o segundo número é 0')
    else:
        divisao = n1/n2
        print(f'A divisão do primeiro número pelo segundo é {divisao:.2f}')
else:
    print('Digite uma opção válida!!!')

