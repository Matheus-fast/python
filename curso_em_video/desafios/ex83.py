# sem usar lista

""" exp = str(input('Digite uma expressão para análise: ')).strip()

aberto = 0
fechado = 0

for letra in exp:

    if letra == '(':
        aberto += 1
    elif letra == ')':
        fechado += 1

if aberto == fechado:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')


 """

# usando lista

exp = list(map(str, input('Digite uma expressão para análise: ').strip()))

parenteses = []

for i in exp:

    if i == '(':
        parenteses.append(i)
    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
    
if len(parenteses) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta.')
