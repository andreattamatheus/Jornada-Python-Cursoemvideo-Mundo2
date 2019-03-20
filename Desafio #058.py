from random import randint
print('='*35)
print('Eu pensei em um número de 0 a 10...')
print('='*35)
num = int(input('Em que número eu pensei?  '))
computador = randint(0,10)
tentativa = 0
while num != computador:
    num = int(input('\033[31mOpção errada, tente novamente.\033[m\nEm que número eu pensei? '))
    tentativa += 1
print('Você acertou, mas precisou de {} tentativa(s).'.format(tentativa+1))