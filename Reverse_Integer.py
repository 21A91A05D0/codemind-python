n=int(input())
r,f=0,0
if n<0:
    f=1
    n=abs(n)
while n:
    d=n%10
    r=r*10+d
    n=n//10
if f==0:
    print(r)
else:
    print('-%d' %r)