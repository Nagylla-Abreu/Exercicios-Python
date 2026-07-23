"""
Dada uma letra, escreva na tela se esta letra é uma vogal ou não.
"""

# verificar se é númerico; se não, retornar LETRA INVÁLIDA.
# transformar a variavel letra em LOWER, caso o usuario digite em maiúscula.

letra = input('Escreva uma letra: ')

letra_minusc = letra.lower()
alpha = letra_minusc.isalpha()

if alpha == True:
    if letra_minusc == 'a' or letra_minusc == 'e' or letra_minusc == 'i' or letra_minusc == 'o' or letra_minusc == 'u':
        print(f'A letra {letra} é uma vogal.')
    else: 
        print(f'A letra {letra} é uma consoante.')
else:
    print('Letra inválida!')