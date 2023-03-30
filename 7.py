a = int(input())
c = 0
d = -1
e = 1
f = 1
g = a
b = [[0 for i in range(a)]for j in range(a)]

while a>0:
    for m in range(a):
        d += e
        b[c][d] += f
        f += 1
    a -= 1
    for n in range(a):
        c += e
        b[c][d] += f
        f += 1
    e *= -1

for x in range(g):
    for y in range(g):
        print(b[x][y], end=' ')
    print()
