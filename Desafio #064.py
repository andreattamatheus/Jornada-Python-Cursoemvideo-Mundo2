num = int(input('Digite um valor qualquer: '))
cont = 0
pra = 0
piru = 0
while cont != 999:
     soma = num + pra
     num = int(input('Digite um valor qualquer: '))
     if num == 999:
         cont = 999
     pra = soma
     piru += 1
print('Foi somado {} número(s) com somatório igual a {}.'.format(piru,soma))