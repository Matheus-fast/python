"""peso = float(input('Peso da 1° pessoa: '))

maior = peso
menor = peso

for n in range (2,6):   
    peso = float(input('Peso da {}° pessoa: '.format(n)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))"""




maior = 0
menor = 0

for n in range (1,6):   
    peso = float(input('Peso da {}° pessoa: '.format(n)))
    
    if n == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))