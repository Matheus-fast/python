while True:
    print('-'*40)
    t = int(input('Quer ver o valor de qual tabuada?: '))
    if t < 0:
        break
    for n in range (0, 11):
        print('{} x {} = {}'.format(t, n, n*t))
print('TABUADA ENCERRADA!')