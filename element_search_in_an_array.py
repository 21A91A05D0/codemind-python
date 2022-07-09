n=int(input())
ls=list(map(int,input().split()))
k=int(input())
c=0
for i in ls:
    if k==i:
        c=1
if c==1:
    print('True')
else:
    print('False')