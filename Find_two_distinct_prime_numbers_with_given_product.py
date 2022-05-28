def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return n

n=int(input())
c=0
for i in range(1,n):
    for j in range(1,n):
        if isprime(i)*isprime(j)==n:
            c=1
            print(i,end=' ')
            break
if c==0:
    print(-1)