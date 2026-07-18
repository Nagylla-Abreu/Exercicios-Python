d = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

ad = d * 60
akm = km * 0.15 
total = ad + akm

print(f'O total a pagar é de R${total:.2f}')