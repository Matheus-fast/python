from datetime import date

ano = int(input('Digite o ano que você nasceu: ')) 
anoAtual = 2017
idade = anoAtual - ano

if idade >= 18:
    alistamento = idade-18
    data = anoAtual - alistamento
    print('Você nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))
    print('Você já deveria ter se alistado há {} anos'.format(alistamento))
    print('Seu alistamento foi em {}'.format(data))
    
elif idade < 18:
    alistamento = ano + 18
    data = (anoAtual - alistamento) * -1  
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))
    print('Ainda faltam {} anos para o alistamento.'.format(data))
    print('Seu alistamento será em {}'.format(alistamento))

else:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))
    print('Você tem que se alistar \033[31mIMEDIATAMENTE\033[m')