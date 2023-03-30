c, r = map(int,input().split())
w = int(input())
a = [[0 for i in range(c)] for j in range(r)]
x = r-1
y = 0
sw=-1
cnt=0
for i in range(c*r):
    for j in range(r):
        cnt += 1
        a[y][x] += cnt
        x += sw
        r -= 1
    sw *= -1
    for z in range(c):
        cnt += 1
        a[y][x] += cnt
        y += sw
        c -= 1
for n in range(r):
    for m in range(c):
        if a[n][m] == w:
            print(m, r-n+1)

        
        
