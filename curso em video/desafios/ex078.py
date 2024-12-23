valores = [] 

c = 0

for v in range(0, 5):
    valores.append(int(input(f'Digite o valor da {c}° posição: ')))
    c += 1

maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi: {maior} nas posições: ', end=' ')
for c, i in enumerate(valores):  
    if i == maior:
        print(f'{c}...', end=' ')

print(f'\nO menor valor digitado foi: {menor} nas posições: ', end=' ')
for c, i in enumerate(valores):
    if i == menor:
        print(f'{c}...', end=' ')
