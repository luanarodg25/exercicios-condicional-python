import math
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print("====== MENU ======")
print("1 -> O primeiro número elevado ao segundo número")
print("2 -> Raiz quadrada de cada um dos números")
print("3 -> Raiz cúbica de cada um dos números")
print()
escolha = int(input('Informe a opção desejada: '))
print()

if escolha == 1:
    resultado = n1**n2
    print(f'Resultado: {resultado}')
elif escolha == 2:
    raiz1 = math.sqrt(n1)
    raiz2 = math.sqrt(n2)
    print(f'Raiz de {n1} é {raiz1:.2f}')
    print(f'Raiz de {n2} é {raiz2:.2f}')
elif escolha == 3:
    cub1 = math.cbrt(n1)
    cub2 = math.cbrt(n2)
    print(f'Raiz cúbica de {n1} é {cub1:.2f}')
    print(f'Raiz cúbica de {n2} é {cub2:.2f}')
else:
    print('Opção inválida!!!')
    

    
