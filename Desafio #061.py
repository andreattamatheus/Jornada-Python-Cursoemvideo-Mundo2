termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite uma razão para uma PA: '))
print ('A razão dessa PA é de {}.'.format(razao))
print('Os 10 primeiros termos são:')
soma = termo
print(termo,end=' -> ')
amais = 0

while soma < (termo+((10+outro)-1)*razao):
    soma = soma + razao
    print('{}'.format(soma),'-> ' if soma < (termo+((10+amais)-1)*razao) else '-> PAUSA',end='')
    while soma == (termo+((10+amais)-1)*razao):
        amais = int(input('\nQuantos termos deseja mostrar a mais? '))


print('Acabou')

       # '''while soma < (termo + ((10 + amais) - 1) * razao):
        #    soma = soma + razao
         #   print('{}'.format(soma), '-> ' if soma < (termo + ((10 + amais) - 1) * razao) else '-> PAUSA', end='')
          #  if soma >= (termo + ((10 + amais) - 1) * razao):
           #     amais = int(input('\nQuantos termos deseja mostrar a mais? '))'''