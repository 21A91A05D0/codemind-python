def fun(n):
    s=0
    while(n):
        d=n%10
        s+=d
        n=n//10
    return s

n=int(input())
s=0
while(True):
    r=fun(n)
    if r<10:
        print(r)
        break
    n=r
    