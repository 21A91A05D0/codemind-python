n=int(input())
a=0
b=0
c=1
while(a<n):
    a=b+c
    b=c
    c=a
if a==n:
    print('True')
else:
    print('False')