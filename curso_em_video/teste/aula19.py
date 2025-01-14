""" dados = dict()

dados = {'nome': 'Pedro',
         'idade': 18,
         'sexo': 'M'}

print(dados['nome'])

print('-='*15)

print(dados.values()) # valores
print(dados.keys()) # chaves
print(dados.items()) # tudo junto

print('-='*15)

for v, v in dados.items():
    print(f'O {v} é {v}')
 """
# trabalhando com dicionário dentro de uma lista

""" brasil = []

estado1 = {'uf': 'São Paulo',
           'sigla': 'SP'}

estado2 = {'uf': 'Rio de Janeiro',
           'sigla': 'RJ'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla']) """

estado = {}
brasil = []

for c in range(3):
    estado['uf'] = str(input('Digite o UF do estado: ')).strip()
    estado['sigla'] = str(input('Digite a SIGLA do estado: ')).strip()
    brasil.append(estado.copy())

print(brasil)

for e in brasil:

    for v in e.values():
        print(v, end=' ')
    print()