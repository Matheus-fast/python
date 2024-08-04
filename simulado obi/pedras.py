n = int(input())

numbers = [0] * n

for jogada in range(1, n):

    if jogada % 2 == 1:

        if len(numbers) >= 2:
            numbers.pop()
            numbers.pop()
        else:
            print('Lalic')
            break
    else:

        if len(numbers) >= 1:
            numbers.pop()
        else:
            print('Enzo')
            break