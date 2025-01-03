from faker import Faker
from time import sleep
from random import randint
from operator import itemgetter

fake = Faker('pt_BR')

jogador1 = fake.name()
jogador2 = fake.name()
jogador3 = fake.name()
jogador4 = fake.name()

pessoas = {jogador1: randint(1, 6),
           jogador2: randint(1, 6),
           jogador3: randint(1, 6),
           jogador4: randint(1, 6),
           }

for k, v in pessoas.items():
    print(f'O jogador(a) {k} jogou {v} no dado.')
    sleep(1.3)

print()
print(f'{"RANKING":-^50}')
print()
sleep(0.7)


ranking = sorted(pessoas.items(), key=itemgetter(1), reverse=True)

# o K se refere a posição, e o V ao valor daquela respectiva posição.
for k, v in enumerate(ranking):
    
    print(f'{k+1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.7)
    print('-'*50)
    sleep(0.7)

print()