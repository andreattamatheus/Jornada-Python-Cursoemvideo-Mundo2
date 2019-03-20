peso = float(input('Digite seu peso atual em Kilogramas: '))
altura = float(input('Digite a sua altura em Metros: '))
IMC = (peso/(altura*altura))
if IMC < 18.5:
    print('Seu IMC é de {:.2f}, você está abaixo do peso!'.format(IMC))
elif IMC < 25:
    print('Seu IMC é de {:.2f}, peso ideal!'.format(IMC))
elif IMC < 30:
    print('Seu IMC é de {:.2f}, SOBREPESO!'.format(IMC))
elif IMC < 40:
    print('Seu IMC é de {:.2f}, você está OBESO!'.format(IMC))
elif IMC > 40:
    print('Seu IMC é de {:.2f}, meu amor você está um pé da COVA!'.format(IMC))