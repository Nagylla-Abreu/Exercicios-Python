larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

a = larg * alt
tinta = a / 2

print(f'Sua parece tem a dimensão {larg}x{alt} e sua área é de {a:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.3f}l de tinta.')