print('=' * 30)
print('SEJA BEM VINDO AO BANCO LADRÃO')
print('=' * 30)
print('O caixa eletrônico possui cédulas de  RS$ 50,20,10 e 1.')
num = int(input('Qual será o valor a ser sacado? R$ '))
total = num
ced = 50
cont = 0
cont2 = 0
cont3 = 0
cont4 = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if total >= 20:
            total -= 20
            cont2 += 1
        else:
            if total >= 10:
                total -= 10
                cont3 += 1
            else:
                if total >= 1:
                    total -= 1
                    cont4 += 1
                else:
                    break
if cont > 0:
    print(f'{cont} cédulas de 50 reais.')
if cont2 > 0:
    print(f'{cont2} cédulas de 20 reais.')
if cont3 > 0:
    print(f'{cont3} cédulas de 10 reais.')
if cont4 > 0:
    print(f'{cont4} cédulas de 1 real.')