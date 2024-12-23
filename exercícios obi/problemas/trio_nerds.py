instrumentos = [0] * 3
certos = ['violao', 'bateria', 'piano']

for pos in range(3):
    instrumentos[pos] = str(input('')).strip().lower()

for instrumento in instrumentos:
    if instrumento in certos:
        if instrumentos.count(instrumento) == 1:
            resp = True
        else:
            resp = False
            break
    else:
        resp = False
        break
            
print('S' if resp else 'N')