termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite uma razão para uma PA: '))
print ('A razão dessa PA é de {}.'.format(razao))
print('Os 10 primeiros termos são:')
soma = termo
outro = 0
amais = 10
cont = 1
while amais != 0:
    outro = outro + amais
    while cont <= outro:
        print('{}'.format(soma),end=' -> ')
        soma = soma + razao
        cont += 1
    print('PAUSA')
    amais = int(input('\nQuantos termos deseja mostrar a mais? '))
print('Acabou')

