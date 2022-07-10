def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
f=prime(n)
r,c=0,0
while n>0:
    r+=1
    d=n%10
    if prime(d)==1:
        c+=1
    n=n//10
if c==r and f==1:
    print('Mega Prime')
else:
    print('Not Mega Prime')