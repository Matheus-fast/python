dias = int(input('Quantos dias alugados? ')) 
km = int(input('Quantos Km rodados? '))

carro = 60*dias 
rodado = km*0.15
total = carro + rodado

print('O total a pagar é de \033[35mR${:.2f}\033[m'.format(total))