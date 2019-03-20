a = 0
b = 0
c = 0
opcao = 'S'
while opcao == 'S':
    idade = int(input('Idade: '))
    while idade not in range(1,999):
        idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper()
    if idade >= 18:
        a += 1
    if sexo == 'M':
        b += 1
    if idade < 20 and sexo == 'F':
        c += 1
    opcao = str(input('Quer continuar? [S/N]')).upper()
    if opcao == 'N':
        break
if a > 1:
    print(f'Existem {a} pessoa(s) com mais de 18 anos.')
else:
    print(f'Existe {a} pessoa cadastrada com mais de 18 anos.')
if b > 1:
    print(f'Foram cadastrados {b} homens.')
else:
    print(f'Foi cadastrado apenas {b} homem.')
if c > 1:
    print(f'Foram cadastradas {c} pessoas com menos de 20 anos.')
else:
    print(f'Foi cadastrado apenas {c} pessoa com menos de 20 anos.')
