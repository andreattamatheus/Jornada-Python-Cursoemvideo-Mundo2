num = int(input('Digite um número inteiro qualquer: '))
print ('Escolha uma base de conversão')
print('''\033[1;33mOpções disponíveis:\033[m
Digite [1] para \033[31mbinário \033[m;
Digite [2] para \033[31moctal \033[m;
Digite [3] para \033[31mhexadecimal \033[m;''')
options = int(input('Opção desejada: '))
if options == 1:
    print('O número {} em binário seria {}'.format(num,bin(num)))
elif options == 2:
    print('O número {} convertido para OCTAL é {}'.format(num,oct(num)))
elif options == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num,hex(num)))
else:
    print('Tente novamente :3')
