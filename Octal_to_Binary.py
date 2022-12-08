from math import pow
t=int(input())
while t:
    n=int(input())
    i=0
    r=0
    while n>0:
        d=n%10
        r+=d*pow(8,i)
        n=n//10
        i+=1
    l,j=0,0
    while r>0:
        d=r%2
        l+=d*pow(10,j)
        r=r//2
        j+=1
    print(int(l))
    t-=1
