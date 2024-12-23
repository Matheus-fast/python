cont = 0
n = 0
soma = 0
r = 's'

while r != 'n':
    soma += n
    cont += 1

    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).lower()

    if cont == 1:
        maior = n
        menor = n

    if n > maior:
        maior = n
    elif n < menor:
        menor = n    

print('Foram digitados {} números, e a média deles foi de: {:.1f}'.format(cont, soma / cont))
print('O maior valor digitado foi: {}, e o menor valor digitado foi: {}'.format(maior, menor))