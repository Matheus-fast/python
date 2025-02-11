# sets:

# - não garantem a ordem
# - não aceitam valores mutáveis, apenas imutáveis
# - seus valores serão sempre únicos
# - não possuem índices

""" s1 = set('Luiz')
s2 = {'1', '2', 3}


print(s1)
print(s2) """


# métodos do set: 
# add, update, clear, discard

# add só aceita adicionar um valor por vez

""" s3 = {1, 2}

s3.add(3)
s3.update(('Matheus', 5, 4))

print(s3)

s3.clear() # limpa o set
print(s3)

s3.discard('Matheus') # limpa um valor específico
print(s3) """

# operadores da matématica que são usados com set

# conseguimos unir, ou union = | 
# fazer interseccção (intersection) com os números presentes em dois sets = &
# apresentar a diferença e mostrar apenas os itens do set à esquerda = -
# e mostrar os valores que não estão presentes em ambos = ^

s4 = {1, 2, 3}
s5 = set()

# s5.add(4, 5, 6)  não pode se adicionar mais de um valor por vez

s5.add(2)
s5.add(3)
s5.add(4)

union = s4.union(s5) # unindo (ou s5 | s6)
intersection = s4 & s5 # mostrando os números presentes nos dois sets
difference = s4.difference(s5) # mostrando os números que só estão no lado esquerdo
difference_simetrical = s4 ^ s5 # mostrando todos os valores que não estão presentes em ambos

print(union)
print(intersection)
print(difference)
print(difference_simetrical)
