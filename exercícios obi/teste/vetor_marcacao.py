numbers = [1, 2, 3, 4, 5, 6]

pares = [0] * len(numbers)

for number in range(len(numbers)):
    
    if number % 2 == 0:
        pares[number] = 1

for number in range(len(numbers)):

    if pares[number] == 1:
        print(f'The number {number} is even')
    else:
        print(f'The number {number} is odd')

    