nome = str(input('Qual é o seu nome completo?')).strip()

print('Seu nome possui Silva? \033[35m{}\033[m'.format('silva' in nome.lower()))