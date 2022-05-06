n=int(input())
t=n
s=0
while(n):
    d=n%10
    s+=d
    n=n//10
if t%s==0:
    print('True')
else:
    print('False')