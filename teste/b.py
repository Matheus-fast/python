t = int(input())    # primeiro dia
m = int(input())    # quantas arvores nascem por dia
a = int(input())    # alvo

arvores = t
sum = 0

while arvores<=a:

    arvores = (arvores*m) + arvores
    sum += 1

print(sum)