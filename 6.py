a = int(input())
n=a//2

for i in range(n+1):
    print(' '*(n-i)*2, end='')
    print('* '*(i*2+1))
for i in range(n-1,-1,-1):
    print(' '*(n-i)*2, end='')
    print('* '*(i*2+1))    

