n=int(input())
n=str(n)
k=len(n)
n=int(n)
r=0
t=n
while n>0:
    d=n%10
    r+=d**k
    n=n//10
    k-=1
if r==t:
    print('True')
else:
    print('False')