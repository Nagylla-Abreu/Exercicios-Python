n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'{n1} + {n2} é igual a {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} * {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print(f'{n1} e {n2} são iguais.')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao != 5: 
        print(f'Escolha inválida. Tente novamente.')
        print('=-==-=' * 5)
print('Programa encerrado.')

