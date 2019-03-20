a = b = c = d = cont = 0
opcao = 'S'
while opcao == 'S':
    nome = str(input('Produto: ')).upper()
    preco = float(input('Preço: R$ '))
    a += preco
    cont += 1
    if preco > 1000:
        b += 1
    if cont == 1 or preco < c:
        c = preco
        d = nome
    opcao = str(input('Deseja continuar: [S/N]')).upper()
    if opcao not in 'SN':
        opcao = str(input('Deseja continuar: [S/N]')).upper()
    if opcao == 'N':
        break
print(f'Total gasto R${a}')
print(f'{b} produtos custam mais que R$1000,00')
print(f'Produto mais barato é {d} que custa R${c}')