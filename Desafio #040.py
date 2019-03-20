media1 = float(input('Digite a nota da sua primeira prova: '))
media2 = float(input('Difite a nota da sua segunda prova: '))
media = (media1+media2)/2

if media <= 4.9:
    print('Sua média é {}, reprovado cuzão!'.format(media))
elif media < 7:
    print('Sua média é {}, recuperação trouxa!'.format(media))
elif media > 7:
    print('Sua média é {}, passou cagão!'.format(media))

