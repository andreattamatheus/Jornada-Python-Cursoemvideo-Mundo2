from time import sleep

print('='*50)
print('Bem vindo ao seu cálculo de gastos!')
print('='*50)

dista = int(input('Qual foi a distância percorrida na sua viagem em Km? '))
sleep(1)
print('Aguarde, estamos calculando o valor da sua viagem...')
sleep(3)
if dista < 200:
    print('O valor da passagem é de R${:0.2f}'.format(dista * 0.5))
else:
    print('O valor da passagem é de R${:0.2f}'.format(dista * 0.45))

print('Have a nice trip!')