num = int(input('Digite um valor: '))
cont = 1
soma = num
while num != 999:
    num = int(input('Digtei outro valor: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} termos é igual a {soma}.')