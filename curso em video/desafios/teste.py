def fizzBuzz(n):

    n = int(input())
    
    for i in range(1, n):
        
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzzz')

fizzBuzz(15)