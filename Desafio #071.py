print('=' * 30)
print('SEJA BEM VINDO AO BANCO LADRÃO!')
print('=' * 30)
#print('O caixa eletrônico possui cédulas de  RS$ 50,20,10 e 1.')
num = int(input('Qual será o valor a ser sacado? R$ '))
total = num
ced = 50
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont != 0:
            print(f'{cont} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total ==0:
            break
