valor = float(input('Digite o preço do seu produto: '))
off = valor - ( valor * 5 / 100)
print('O produto que custava \033[31mR${}\033[m, na promoção com desconto de 5% vai custar \033[32mR${:.2f}\033[m'.format(valor, off))