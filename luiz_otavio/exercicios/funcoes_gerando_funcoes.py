def criar_multiplicador(multiplicador):

    def multiplicar(num):
        return multiplicador * num

    return multiplicar

n = criar_multiplicador(4)
print(n(2))