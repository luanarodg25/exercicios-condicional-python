primeiroN = int(input('Informe o primeiro número: '))
segundoN = int(input('Informe o segundo número: '))

if primeiroN > segundoN:
    print('O',primeiroN,'é maior que',segundoN)
elif segundoN > primeiroN:
    print('O',segundoN,'é maior que',primeiroN)
else:
    print('Os números digitados são iguais')
