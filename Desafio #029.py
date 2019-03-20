
print('='*50)
print('Bem vindo ao DETRAN, estamos aqui para te foder!')
print('='*50)

vel = int(input('Nos informe a velocidade média do seu veículo: '))
per = int('80')
multa = float((vel-per)*7)

if vel > per:
    print('O senhor foi multado devido a velocidade de {} Km/h exceder a permitido de {} Km/h.'.format(vel,per))
    print('O valor da multa aplicada é de R${:.2f}'.format(multa))
else:
    print('O veículo não foi multado, a velocidade máxima permitida é de {} Km/h'.format(per))
print('Tenha um bom dia!')