n=int(input())
p=1
s=0
t=n
while(n>0):
    d=n%10
    p=p*d
    s=s+d
    n=n//10
if p==s:
    print('Spy Number')
else:
    print('Not Spy Number')