num = int(input('Deseja ver a tabuada de qual valor? '))
cont = 1
while num > 0:
    print(f'''1x{num} = {num*1}
2x{num} = {num*2}
3x{num} = {num*3}
4x{num} = {num*4}
5x{num} = {num*5}
6x{num} = {num*6}
7x{num} = {num*7}
8x{num} = {num*8}
9x{num} = {num*9}''''')
    if cont == 1:
        num = int(input('Deseja ver a tabuada de qual valor? '))
        cont = 0
    if num < 0:
            break
    cont += 1
print('PROGRAMA ENCERRADO')