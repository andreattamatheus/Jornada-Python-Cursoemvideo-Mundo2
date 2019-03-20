from random import randint
print('='*35)
print('Eu pensei em um número de 0 a 5...')
print('='*35)
num = int(input('Em que número eu pensei?  '))
computador = randint(0,5)

if num == computador:
    print('Acertou miseravi!!')
else:
    print('Se lascou,o número certo é {}.'.format(computador))
    print('Tente novamente!')
