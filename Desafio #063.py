fibonacci = int(input('Deseja mostrar quantos termos da sequência? '))
primeiro = 0
segundo = 1
if fibonacci != 0:
    print('A sequência de {} elemento(s) ficaria:'.format(fibonacci))
    print('{} -> {}'.format(primeiro,segundo),end=' -> ')
    cont = 3
    while cont <= fibonacci:
       fibo = primeiro + segundo
       print('{}'.format(fibo),end=' -> ')
       primeiro = segundo
       segundo = fibo
       cont += 1
    print('FIM')
else:
    print('Não é possível mostrar 0 elementos!')


