print('-='*15)
print('Analisador de Triângulos: ')
print('-='*15)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os segmentos acima \033[4;32mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[4;31mNÃO PODEM FORMAR\033[m um triângulo!')