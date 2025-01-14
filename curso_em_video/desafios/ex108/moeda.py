def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def metade(valor=0, format=False):
    novoValor = valor / 2
    return novoValor

def dobro(valor=0,):
    novoValor = valor*2
    return novoValor

def acrescimo(valor=0, aumento=1):
    novoValor = (valor / 100) * aumento + valor
    return novoValor

def diminuir(valor=0, diminui=0):
    novoValor = valor - diminui
    return novoValor