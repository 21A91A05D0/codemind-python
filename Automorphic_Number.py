n=int(input())
p=n*n
t=n
g=0
while n>0:
    d=n%10
    g+=1
    n=n//10
x=0
while g>0:
    d=p%10
    x=x*10+d
    p=p//10
    g-=1
rev=0
while x>0:
    d=x%10
    rev=rev*10+d
    x=x//10
if t==rev:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')