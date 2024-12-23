altura = float(input('Qual é a altura da sua parede para pintar? '))
largura = float(input('E qual é a largura da parede para pintar? '))

area = altura*largura
tinta = area/2

print('Sua parede tem a dimensão de \033[36m{}\033[m x \033[35m{}\033[m e sua área é de \033[34m{:.2f}m²\033[m].'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de \033[32m{:.2f}l\033[m de tinta'.format(tinta))