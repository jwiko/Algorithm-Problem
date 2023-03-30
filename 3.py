S=[]

a = int(input())

d=1
for i in range(a):
    b, c = input().split()
    c=int(c)
    S.append((b,c))

for x in range(a):
    for z in range(a):
        if(S[x][1]<S[z][1]):
            d = d + 1
    print(S[x][0], d)
    d=1
