def enfeite(msg):

    tam = len(msg) + 4
    enfeite = '~' * tam

    print(enfeite)
    print(f'{msg:^{tam}}')
    print(enfeite)

def tamanhoMsg(msg):

    print(f'O tamanho da palavra {msg} é {len(msg)}')
