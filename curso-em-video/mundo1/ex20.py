import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]

escolha = random.sample(alunos, 4) 

print(f'A ordem da apresentação será {escolha}')

# há a possibilidade de usar o random.shuffle, mas ele altera a lista original. 
# com o random.sample, há uma sofisiticação maior e te permite escolher quantos irão ser sorteado de um tanto x.


