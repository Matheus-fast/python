def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def metade(valor):
    print(f'A metade de {moeda(valor)} é: {moeda(valor)}')

def dobro(valor):
    print(f'O dobro do valor {moeda(valor)} é: {moeda(valor)}')

def aumento10(valor):
    print(f'O valor {moeda(valor)} com um acrécimo de 10% ficará: {moeda(valor + (valor/100) * 10)}')
