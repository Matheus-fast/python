pessoa = dict()
pessoas = list()
mulheres = []
maioresMedia = []

somaIdade = 0

while True:

    pessoa['nome'] = str(input('Digite seu nome: ')).capitalize().strip()
    pessoa['idade'] = int(input('Digite sua idade: '))
    somaIdade += pessoa['idade']

    pessoa['sexo'] = str(input('Digite seu sexo [M | F]: ')).strip().upper()

    while True: 

        if pessoa['sexo'] not in 'MF':        

            print('ERRO!')
            print('Por favor digite apenas M para masculino ou F para feminino.')
            pessoa['sexo'] = str(input('Digite seu sexo [M | F]: ')).strip().upper()

        else:
            break  

    continuar = str(input('Deseja continuar? [S | N]: ')).lower().strip()

    while True:

        if continuar not in 'sn':
            print('ERRO!')
            print('Por favor digite apenas S para continuar ou N para encerrar o programa.')
            continuar = str(input('Deseja continuar? [S | N]: ')).lower().strip()
        
        else:
            break

    pessoas.append(pessoa.copy())

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

    if continuar == 'n':
        break

mediaIdade = somaIdade / len(pessoas)

for i in pessoas:
    
    if i['idade'] >= mediaIdade:
        maioresMedia.append(i)

print("-="*25)
print(f'{"ANÁLISE DE DADOS":^50}')
print("-="*25)

print(f'A) Ao todo temos {len(pessoas)} cadastradas.')

print(f'B) A média de idade é de {mediaIdade:.2f} anos')

print(f'C) As mulheres cadastradas foram: ', end='')

if len(mulheres) == 0:
    print('Não existe mulhers cadastradas.')

else: 

    for pos, nome in enumerate(mulheres):
        
        max = len(mulheres)

        if (pos+1) == max:
            print(f'{nome}.')   

        else: 
            print(nome, end=', ')

print(f'D) Lista das pessoas que estão acima da média:')

for lista in maioresMedia:

    for k, v in lista.items():
        print(f'{k} = {v}', end='; ')
    print()
