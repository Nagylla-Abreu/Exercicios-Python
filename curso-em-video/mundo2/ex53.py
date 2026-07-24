# juntar a frase sem espaços e deixar tudo maiúsculo.
# usar função de inverter 

frase = input('Digite uma frase para verificar se é um palíndromo: ')

frasemaiusc = frase.upper()
frasenospace = frasemaiusc.replace(' ', '')
fraseinv = frasenospace[::-1]

print(f'O inverso de {frasenospace} é {fraseinv}')

if frasenospace == fraseinv:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase NÃO é um palíndromo')