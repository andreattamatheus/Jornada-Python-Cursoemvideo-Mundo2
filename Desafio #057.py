sexo = str(input('Digite o seu sexo: (M/F) ')).upper()
while sexo not in 'MF':
    sexo = str(input('Opção inválida, digite novamente o seu sexo: (M/F) ')).upper()
if sexo == 'M':
    print('Você é do sexo masculino.')
elif sexo == 'F':
    print('Você é do sexo feminino.')