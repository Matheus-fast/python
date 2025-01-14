times = ( 'Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro', 'Atlético-MG',
'Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco', 'Criciúma',
'Juventude', 'Corinthians', 'Fluminense', 'Vitória', 'Atlético-GO', 'Cuiabá')

print(f'\nLISTA DE TIMES BRASILEIROS: {times}\n')
print('-='*48)

print(f'\nOs cinco primeiros times são: {times[:5]}\n')
print('-='*48)

print(f'\nOs últimos 4 times são: {times[-4:]}\n')
print('-='*48)

print(f'\nA tabela do Brasileirão em ordem alfabética é: {sorted(times)}')
print('-='*48)

print(f'\nO time São Paulo está na: {times.index("São Paulo") +1}° colocação')