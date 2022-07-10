n=int(input())
ls=list(map(int,input().split()))
c,d=0,0
for i in range(0,n):
    if ls[i]%2!=0 and i%2!=0:
        c+=1
    if ls[i]%2!=0:
        d+=1
if c==d:
    print('True')
else:
    print('False')