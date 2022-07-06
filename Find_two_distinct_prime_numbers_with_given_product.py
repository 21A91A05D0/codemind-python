def prime(n):
    if n==1:
        return 0 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    return n

n=int(input())
c=0
for i in range(1,n):
    for j in range(1,n):
        if prime(i)*prime(j)==n:
            c=1
            print(i,end=' ')
if c==0:
    print('-1')
            