from math import pow
t=int(input())
while t:
    n=int(input())
    i=0
    r=0
    while n>0:
        d=n%10
        r+=d*pow(2,i)
        n=n//10
        i+=1
    print(int(r))
    t-=1
