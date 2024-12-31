# abaixo de 5 = reprovado
# entre 5 e 7 = recuperação
# acima de 7 = aprovado

pessoa = {}

pessoa['nome'] = str(input('Qual o nome do aluno? ')).capitalize()
pessoa['media'] = float(input(f'Qual a média do: {pessoa["nome"]}? '))

print('-='*20)

""" print(f'    -- NOME: {pessoa['nome']}')
print(f'    -- MÉDIA: {pessoa['media']}')
print(f'    -- SITUAÇÃO:', end=' ')

if pessoa['media'] < 5:
    print('REPROVADO')

elif pessoa['media'] < 7:
    print('RECUPERAÇÃO')

else:
    print('APROVADO') """

if pessoa['media'] < 5:
    pessoa['situacao'] = 'REPROVADO'

elif pessoa['media'] < 7: 
    pessoa['situacao'] = 'RECUPERAÇÃO'

else:
    pessoa['situacao'] = 'APROVADO'

for k, v in pessoa.items():
    print(f'  -- {k.upper()}:', end= ' ')
    print(f'{v}')

