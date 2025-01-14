def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def metade(valor=0, format=False):
    novoValor = valor / 2
    return novoValor if not format else moeda(novoValor)

def dobro(valor=0, format=False):
    novoValor = valor*2
    return novoValor if format is False else moeda(novoValor)

def acrescimo(valor=0, aumento=1, format=False):
    novoValor = (valor / 100) * aumento + valor
    return novoValor if format is False else moeda(novoValor)

def diminuir(valor=0, diminui=0, format=False):
    novoValor = valor - diminui
    return novoValor if format is False else moeda(novoValor)