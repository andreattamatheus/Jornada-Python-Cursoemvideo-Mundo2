n1 = int(input('Digite o primerio valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
#Aqui temos o valor maior"
if n1 > n2 and n3:
    print('O maior valor é {}'.format(n1))
else:
    if n2 > n3:
        print('O maior valor é {}'.format(n2))
    else:
        print('O maior valor é {}'.format(n3))
# Aqui temos o valor menor
if n1 < n2 and n3:
    print('O menor valor é {}'.format(n1))
else:
    if n2 < n3:
        print('O menor valor é {}'.format(n2))
    else:
        print('O menor valor é {}'.format(n3))
