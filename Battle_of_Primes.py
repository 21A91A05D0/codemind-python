def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

n1=int(input())
n2=int(input())
s=n1+n2
k=0
i=1
while s>0:
    if isprime(s+i)==1:
        k=(s+i)
        break
    i+=1
d=k-s
print(d)