import copy # importanto a biblioteca principal

# criando a lista principal
pessoa = {
    'nome': 'Matheus',
    'sobrenome': 'Oliveira',
    'endereco': ['rua marques de lages', 'rua aricanduva']
}

pessoa_shallowCopy = copy.copy(pessoa) # Shallow Copy
pessoa_deepCopy = copy.deepcopy(pessoa) # Deep Copy

print(f'A lista principal é: {pessoa}')
print(f'A lista com Shallow Copy é: {pessoa_shallowCopy}')
print(f'A lista com Deep Copy é: {pessoa_deepCopy}')

pessoa_shallowCopy['endereco'][1] = 'rua belo horizonte' # vai alterar a lista principa (pessoa).
pessoa_deepCopy['endereco'][0] = 'rua manaus' # vai alterar somente no pessoa 3, pois é uma deep copy.
print()

print(f'A lista principal é: {pessoa}') # agora pessoa tem o seu endereço mudado, pois foi mudado na pessoa_shallowCopy, que fez uma Shallow Copy
print(f'A lista com Shallow Copy é: {pessoa_shallowCopy}')
print(f'A lista com Deep Copy é: {pessoa_deepCopy}')

""" pessoa.setdefault('idade', 18) # caso a chave não exista, irá ser criado um valor padrão
 
print(pessoa['idade']) """