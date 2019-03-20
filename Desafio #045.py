from random import randint
from time import sleep

print('=' * 50)
print('WELCOMEEEEEEEE TO JUMANJIIIIIIII. FIRST, SELECT YOUR CHARACTER!')
print('Just kidding :3')
print('=' * 50)

print('''Vamos jogar um pouco, as opções estão dividas assim: 
[1] PEDRA;
[2] PAPEL;
[3] TESOURA;''')

user = int(input('Choose your hand MDF: '))
rival = int(randint(1,3))

print('Resultados em instantes.... Computador escolhendo a jogada...')
sleep(2)

# PRIMEIRA CONDIÇÃO
if user == 1 and rival == 1:
    print('Você jogou PEDRA, o computador PEDRA => EMPATE!')
elif user == 1 and rival == 2:
    print('Você jogou PEDRA, o computador PAPEL => VOCÊ PERDEU!')
elif user == 1 and rival == 3:
    print('Você jogou PEDRA, o computador TESOURA => VOCÊ GANHOU!')

#SEGUNDA CONDIÇÃO
if user == 2 and rival == 1:
    print('Você jogou PEDRA, o computador PAPEL => VOCÊ PERDEU!')
elif user == 2 and rival == 2:
    print('Você jogou PAPEL, o computador PAPEL => EMPATE!')
elif user == 2 and rival == 3:
    print('Você jogou TESOURA, o computador PAPEL => VOCÊ GANHOU !')

# TERCEIRA CONDIÇÃO
if user == 3 and rival == 1:
    print('Você jogou PEDRA, o computador TESOURA => VOCÊ GANHOU!')
elif user == 3 and rival == 2:
    print('Você jogou PAPEL, o computador TESOURA => VOCÊ PERDEU!')
elif user == 3 and rival == 3:
    print('Você jogou TESOURA, o computador TESOURA => EMPATE!')