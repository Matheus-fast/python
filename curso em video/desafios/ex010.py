din = float(input('Quanto de dinheiro você possui em real na carteira?'))
dol = din / (5.26)
print('Com \033[33mR${}\033[m você pode comprar \033[32mU${:.2f}\033[m'.format(din, dol))