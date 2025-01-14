""" def voto(ano):

    from datetime import date

    # para descobrir o ano atual
    anoAtual = date.today().year

    idade = anoAtual - ano

    if idade < 16:
        return f'Com {idade} anos, você possui voto proibido.'
    
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos, você possui Voto opcional.'
    
    else:
        return f'Com {idade} anos, você possui Voto obrigatório.'
    
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc)) """

print('\033[37;41mTexto branco com fundo vermelho\033[m')
print('\033[31;47mTexto vermelho com fundo branco\033[m')
print('\033[30;47mTexto preto com fundo branco\033[m')

