def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f    

n=int(input())
t=n
s=0
while(n):
    d=n%10
    s=s+fact(d)
    n=n//10
if s==t:
    print('The number %d is a strong number' %t)
else:
    print('The number %d is not a strong number' %t)