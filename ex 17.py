try:
    senha = int(input('Digite a senha (somente números): '))
    if senha == 4531:
        print('Senha correta, acesso liberado ;)')
    else:
        print('Senha incorreta, tente novamente.')
except ValueError:
    print('Entrada inválida! A senha deve conter apenas números.')
