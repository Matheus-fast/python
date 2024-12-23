from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(tupla)
print(f'O menor valor gerado foi: {min(tupla)}')
print(f'O maior valor gerado foi: {max(tupla)}')