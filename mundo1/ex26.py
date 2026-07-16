frase = input('Digite uma frase: ')

frasemin = frase.lower()
frasenospace = frasemin.strip()

print(f'A letra A aparece {frasenospace.count('a')} vezes na frase.')
print(f'A letra A apareceu na posição {frasenospace.find('a')+1}')
print(f'A última letra A apareceu na posição {frasenospace.rfind('a')+1}')