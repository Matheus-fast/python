lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # -1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8], # 8
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7], # -1
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], # 7
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7], # -1
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9], # 9
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1], # 1
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3], # -1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7], # 5
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1], # -1
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7], # 8
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], # -1
]

numeros_duplicados = []

for lista in lista_de_listas_de_inteiros:

    numeros_repetidos = set()

    for indice, numero in enumerate(lista):
        
        if lista.count(numero) >= 2:
            numeros_repetidos.add(numero)
        
        tamanho_set_repetido = len(numeros_repetidos)

        if tamanho_set_repetido == 3:
            numeros_duplicados.append(numero)
            break

        if tamanho_set_repetido < 3 and indice == len(lista) -1:
            numeros_duplicados.append(-1)
            break

    numeros_repetidos.clear()
    
print(numeros_duplicados)
