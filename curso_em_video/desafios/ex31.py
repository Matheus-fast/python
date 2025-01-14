dis = int(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.2f}'.format(dis))

if dis >= 200:
    preco = dis * 0.45
    print('E o \033[4;32mpreço\033[m da sua passagem será de \033[35mR${:.2f}\033[m'.format(preco))
else:
    preco = dis * 0.50
    print('E o \033[4;32mpreço\033[m da sua passagem será de \033[34mRS${:.2f}\033[m'.format(preco))