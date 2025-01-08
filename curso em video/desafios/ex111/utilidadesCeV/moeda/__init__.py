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

def resumo(valor, juros, reducao):

    print('-'*38)
    print(f'{"RESUMO DO PREÇO":^38}')
    print('-'*38)

    print(f'{"Preço analisado: ":<25}{moeda(valor):<30}')
    print(f'{"Dobro do preço: ":<25}{moeda(dobro(valor)):<30}')
    print(f'{"Metade do preço: ":<25}{moeda(metade(valor)):<30}')
    print(f'{f"{juros}% de aumento:":<24} {moeda(acrescimo(valor, juros)):<29}')
    print(f'{f"{reducao}% de redução:":<24} {moeda(diminuir(valor, reducao)):<29}')

    print(f'-'*38)