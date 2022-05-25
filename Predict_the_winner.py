n=int(input())
ls=list(map(int,input().split()))
s,d=0,0
for i in range(0,n):
    if i%2==0:
        s+=ls[i]
    if i%2!=0:
        d+=ls[i]
j=abs(d-s)
if j%4==0:
    print('X')
else:
    print('Y')