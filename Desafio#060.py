
'''num = int(input('Digite um número qualquer: '))
fatorial = 1
for num in range(num,1,-1):
    fatorial = fatorial*num
print(fatorial)'''
#exercicio com uso do FOR IN RANGE

num = int(input('Digite um número qualquer: '))
fatorial = num
c = 1
print('{}! = '.format(num),end='')
while fatorial > 0:
    print('{}'.format(fatorial), end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    c = c * fatorial
    fatorial = fatorial - 1
print(c,end='')