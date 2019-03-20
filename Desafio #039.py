from datetime import date

nascimento = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year

idade = atual - nascimento

if idade == 18:
    print('Você nasceu em {}, sendo assim você tem {} anos e deve se alistar esse ano!'.format(nascimento, idade))
elif idade > 18:
    print('Você nasceu em {}, seu prazo para se alistar era até {}!'.format(nascimento, nascimento + 18))
else:
    print('Você nasceu em {}, você deverá se alistar em {}'.format(nascimento, nascimento + 18))

