instrumentos = [0] * 3
certos = ['violao', 'bateria', 'piano']

for pos in range(3):
    instrumentos[pos] = str(input('')).strip().lower()

for instrumento in instrumentos:

        if instrumentos.count(instrumento) > 1:
            resp = False
            break
        else:
            resp = True
            
print('S' if resp == True else 'N')