n = int(input())
m = int(input())

resp = 0
v = [0] * (n+1)
for _ in range(m):
    x = int(input())
    v[x] = 1

for x in range(1, n+1):
    if v[x]==0:
        resp+=1

print(resp)