def calcularArea(l, c):

    a = l*c

    print(f'A área de um terreno {l}x{c} é de {a:}m².')

print('CONTROLE DE TERRENOS')
print('-'*20)

larg = float(input('Largura (M): '))
comp = float(input('Comprimento (M): '))

calcularArea(larg, comp)