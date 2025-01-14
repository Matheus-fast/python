s = 0
cont = 0

for n in range (1, 500, 2):
    if n % 3 == 0:
        s += n
        cont = cont + 1
print('A soma de todos os {} numeros ímpares vai ser {}'.format(cont, s))