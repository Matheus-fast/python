soma = 0
cont = 0
n = 0

n = int(input('Digite um número [999 PARA PARAR]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 PARA PARAR]: '))
print('Você digitou {} números, e a soma entre eles é de {}'.format(cont, soma))