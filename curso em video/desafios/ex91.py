from faker import Faker
from time import sleep
from random import randint
from operator import itemgetter

fake = Faker('pt_BR')

jogador1 = fake.name()

pessoas = {}

pessoas[jogador1]

print()
print(f'{"RESULTADO":-^50}')
print()

# ranking = sorted(pessoas.items(), key=itemgetter(1), reverse=True)

# print(ranking)

print()