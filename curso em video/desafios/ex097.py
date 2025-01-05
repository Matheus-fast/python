def escreva(msg):

    tam = len(msg) + 4
    enfeite = '~' * tam

    print(enfeite)
    print(f'{msg:^{tam}}')
    print(enfeite)

escreva('Hello, World')
escreva('Olá, Mundo')
escreva('Olá, Matheus')