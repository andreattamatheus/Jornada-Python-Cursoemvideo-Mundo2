preco = float(input('Digite o valor do produto: R$ '))
print('''Condições de pagamento:
      [1] Á vista DINHEIRO/CHEQUE 
      [2] 1x CARTÃO
      [3] 2x CARTÃO
      [4] 3x ou mais no CARTÃO''')
con = int(input('Forma de pagamento desejada: '))

if con == 1:
    print('O valor a ser pago pelo produto é de R${:.2f}'.format(preco*1.1))
elif con == 2:
    print('O valor a ser pago pelo produto é de R${:.2f}'.format(preco*1.05))
elif con == 3:
    print('O valor a ser pago pelo produto é de R${:.2f}'.format(preco))
elif con == 4:
    print('O valor a ser pago pelo produto é de R${:.2f}'.format(preco*1.2))