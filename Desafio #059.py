valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
menu = str(input('[1] Soma\n'
                 '[2] Multiplicar\n'
                 '[3] Saber qual o maior\n'
                 '[4] Novos números\n'
                 '[5] Sair do programa\n'
                 '\033[31mQual operação deseja realizar?\033[m'))
while menu in '1234':
    if menu == '1':
        print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
    elif menu == '2':
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
    elif menu == '3':
        if valor1 > valor2:
            print('O valor {} é maior que {}'.format(valor1,valor2))
        elif valor2 > valor1:
            print('O valor {} é maior que {}'.format(valor2,valor1))
    elif menu == '4':
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        menu = str('Qual operação desejada da lista?')
    print('=' * 40)
    menu = str(input('[1] Soma\n'
                     '[2] Multiplicar\n'
                     '[3] Saber qual o maior\n'
                     '[4] Novos números\n'
                     '[5] Sair do programa\n'
                     '\033[31mQual operação deseja realizar?\033[m'))
print('Programa encerrado!')