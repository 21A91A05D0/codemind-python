def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

t=int(input())
for j in range(1,t+1):
    n=int(input())
    k=n
    i=1
    while n>0:
        if isprime(n+i)==1:
            l=n+i
            break
        i+=1
    for i in range(n,1,-1):
        if isprime(i)==1:
            h=i
            break
    a=l-k
    b=k-h
    if a>=b:
        print(h)
    else:
        print(l)