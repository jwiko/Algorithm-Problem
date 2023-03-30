a, b = map(int,input().split())

def prime(n):
    if(n==1):
        return False
    for i in range(2, n):
        if(n%i==0):
            return False
    return True




for i in range(a, b+1):
    if(prime(i)):
        print(i, end=' ')
            
         



