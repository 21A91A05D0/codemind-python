n=int(input())
ls=list(map(int,input().split()))
c=0
for i in ls:
    if i%2==0:
        c+=1
if c==n:
    print('True')
else:
    print('False')