primeiro = int(input('Digite um valor: '))
segundo = int(input('Digite outro valor: '))

if primeiro > segundo:
    print('O valor {} é maior que {}!'.format(primeiro,segundo))
elif primeiro < segundo:
    print('O valor {} é maior que {}!'.format(segundo,primeiro))
elif primeiro == segundo:
    print('O valor [} é igual ao {}'.format(primeiro,segundo))
else:
    print('Informações inválidas, tente novamente.')