from time import sleep

print('='*50)
print('Let´s learn something new!!!')
print('='*50)

ano=int(input('Digite um ano se sua preferência: '))
sleep(1)
print('Carregando...')
sleep(2)

if ((ano%4) == 0) and ano%100!=0 or ((ano%400) == 0):
    print('{} é ano bissexto!'.format(ano))
else:
    print('{} não é ano bissxeto!'.format(ano))

