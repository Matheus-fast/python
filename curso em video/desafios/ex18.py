from math import radians, sin, cos, tan
angulo = float(input('Ditite o ângulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo \033[34m{}\033[m tem o SENO de \033[32m{:.2f}\033[m'.format(angulo, seno))
print('O angulo de \033[33m{}\033[m tem o COSSENO de \033[32m{:.2f}\033[m'.format(angulo, cosseno))
print('O angulo de \033[35m{}\033[m tem a tangente de \033[32m{:.2f}\033[m'.format(angulo, tangente))