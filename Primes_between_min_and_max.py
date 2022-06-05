from math import sqrt
def isprime(n):
    if n==1:
        return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
ls=list(map(int,input().split()))
b=ls.index(max(ls))
a=ls.index(min(ls))
c=0
if a<b:
    for i in range(a,b+1):
        if isprime(ls[i])==1:
            c+=1
else:
    for i in range(b,a+1):
        if isprime(ls[i])==1:
            c+=1
    
print(c)