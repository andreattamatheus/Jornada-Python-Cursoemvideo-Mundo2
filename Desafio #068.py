from random import randint
num = int(input('Digite um valor: '))
opcao = str(input('Par ou Ímpar? [P/I] ')).upper()
maquina = randint(0,10)
resultado = num + maquina
cont = 0
while opcao not in 'PI':
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper()
    if opcao == 'P':
        if resultado % 2 == 0:
            print(f'Você escolheu {num} e o computador {maquina}. Total de {resultado} deu PAR.')
            print('Você venceu!')
            print('=' * 30)
            cont += 1
            num = int(input('Digite um valor: '))
            opcao = str(input('Par ou Ímpar? [P/I] ')).upper()
        else:
            print((f'Você escolheu {num} e o computador {maquina}. Total de {resultado} deu ÍMPAR.'))
            print('Você perdeu!')
            print('=' * 30)
            break
    if opcao == 'I':
        if resultado % 2 == 0:
            print(f'Você escolheu {num} e o computador {maquina}. Total de {resultado} deu PAR.')
            print('Você perdeu!')
            print('=' * 30)
            break
        else:
            print((f'Você escolheu {num} e o computador {maquina}. Total de {resultado} deu ÍMPAR.'))
            print('Você venceu!')
            print('=' * 30)
            cont += 1
            num = int(input('Digite um valor: '))
            opcao = str(input('Par ou Ímpar? [P/I] ')).upper()
print(f'GAME OVER. Você venceu {cont} vezes.')

