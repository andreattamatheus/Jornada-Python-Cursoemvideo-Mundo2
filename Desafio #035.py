n1 = float(input('Digite o primerio comprimento: '))
n2 = float(input('Digite o segundo comprimento: '))
n3 = float(input('Digite o terceiro comprimento: '))
valor1 = n2 - n3
valor2 = n1 - n3
valor3 = n1 - n2
if abs(valor1) < n1 < n2+n3 or abs(valor2) < n2 < n1+n3 or abs(valor3) < n3 < n1+n2:
    print('Com os valores informados é possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo com os valores informados!')