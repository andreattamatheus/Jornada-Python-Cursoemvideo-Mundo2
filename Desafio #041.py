from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - nascimento
if idade < 9:
    print('Você tem {} anos, sua categoria é MIRIM!'.format(idade))
elif idade < 14:
    print('Você temm {} anos, sua categoria é INFANTIL!'.format(idade))
elif idade < 19:
    print('Você tem {} anos, sua categoria é JUNIOR!'.format(idade))
elif idade < 20:
    print('Você tem {} anos, sua categoria é SÊNIOR!'.format(idade))
elif idade > 20:
    print('Você tem {} anos, sua categoria é MASTER!'.format(idade))