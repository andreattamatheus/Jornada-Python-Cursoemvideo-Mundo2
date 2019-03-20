salario = int(input('Digite o valor do seu salário em R$: '))
if salario > 1250:
    print('O valor do seu aumento é de R${:0.2f}'.format(salario*1.1))
else:
    print('O valor do seu aumento é de R${:0.2f}'.format(salario*1.15))