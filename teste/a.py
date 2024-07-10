e = int(input())
a = int(input())
c = int(input())

et = e*2
at = a*3
ct = c*5

media = et + at + ct


if media >= 200:
    print('O')

elif media >= 150 and media < 200:
    print('S')

elif media >= 100 and media < 150:
    print('B')

else:
    print('N')