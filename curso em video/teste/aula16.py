lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#print(lanche[:3])

for c in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c+1}')
print('Comi pra caramba!')

"""for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')"""

"""for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos+1}')"""

# print(sorted(lanche))