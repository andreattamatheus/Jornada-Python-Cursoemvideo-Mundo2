# coding=utf-8
num = int(input('Digite um valor qualquer: '))
pergunta = 'S'
pra = 0
piru = int(0)
menor = num
maior = 0
while pergunta != 'N':
     soma = num + pra
     pergunta = str(input('Deseja continuar? [S/N]')).upper()
     while pergunta != 'S' and pergunta != 'N':
         pergunta = input('Opção inválida, favor tentar novamente: [S/N]').strip().upper()[0]
     if maior < num:
         maior = num
     if menor > num:
         menor = num
     if pergunta == 'S':
        num = int(input('Digite outro valor qualquer: '))
        pra = soma
     piru += 1
print('A média dos {} valores foi de {}'.format(piru,soma/piru))
print ('O maior valor é {} e o menor é {}.'.format(maior,menor))