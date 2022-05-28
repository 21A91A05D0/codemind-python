n=int(input())
h,c,g=0,0,0
while n>0:
    h+=1
    d=n%10
    if d%2==0:
        c+=1
    if d%2!=0:
        g+=1
    n=n//10
if c==h:
    print('Even')
if g==h:
    print('Odd')
if c<h and g<h:
    print('Mixed')