import random

valores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = random.sample(valores, k=5)
maior = max(result)
menor = min (result)
print(f'Os valores sorteados foram: {result}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')