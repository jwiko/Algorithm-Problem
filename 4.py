import random

a = int(input())
b = [0,0,0,0,0,0]
for i in range(a):
    d = random.randint(1,6)
    b[d-1] = b[d-1] + 1

for x in range(6):
    print(x+1, b[x], round((b[x]/a)*100, 2))
