frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece \033[31m{}\033[m vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição: \033[34m{}\033[m'.format(frase.find('a')+1))
print('A última letra A apareceu na posição \033[36m{}\033[m'.format(frase.rfind('a')+1))