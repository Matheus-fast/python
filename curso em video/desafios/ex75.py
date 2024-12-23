a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

tupla = (a, b, c, d)

print(f'Você digitou os números: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O número 3 apareceu pela primeira vez na posição: {tupla.index(3)+1}')
else:
    print(f'O valor 3 não foi digitado')

print('Os valores pares digitados foram: ', end='')

for i in tupla: 
    if i%2 == 0:
        print(i, end=' ')