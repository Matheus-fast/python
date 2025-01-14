from datetime import date

# nome, ano de nascimento e carteira de trabalho
# se carteira for = 0, programa encerra, se não:
# ano de contratação e Salárioário
# falar o ano em que a pessoa irá se aposentar após 35 anos de contribuição

data = date.today()
ano = data.year

pessoa = dict()

pessoa['nome'] = str(input('Digite seu nome: ')).capitalize().strip()
pessoa['idade'] = int(input('Digite seu ano de nascimento: '))
pessoa['ctps'] = int(input('Digite o número da sua carteira de trabalho: '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - pessoa['idade']) + 35
    pessoa['Salário'] = float(input('Digite o salário atual: R$'))

    pessoa['idade'] = ano - pessoa['idade']

print('-='*20)
for k, v in pessoa.items():
    print(f'  -- {k.capitalize()} tem valor: {v}')