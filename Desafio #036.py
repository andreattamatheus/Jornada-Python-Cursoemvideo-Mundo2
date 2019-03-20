from time import sleep
print('='*50)
print('Welcome to your favorite banking simulator!')
print('='*50)

casa = float(input('What is the price of the desired house? '))
salario = float(input('Whats your current salary? '))
anos = int(input('How many years do you intend to pay for it? '))
meses = anos*12
prestacao = (casa/meses)
#sleep(1)
#print('Processing data...')
#sleep(2)
if prestacao <= (salario*0.3):
    print('Loaned money approved, the house installment will be R${:.2f} per month!'.format(prestacao),end=' ')
else:
    print('Loan denied, the installment calculeted of R${:.2f}, exceed the permissible limit.'.format(prestacao))

print('Have a nice day!')