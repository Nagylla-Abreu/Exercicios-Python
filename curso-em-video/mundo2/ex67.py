while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 15)
    cont = 1
    if num < 0:
        break
    while cont <= 10:        
            print(f'{num} x {cont} = {num*cont}')
            cont += 1
    print('-' * 15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        
    