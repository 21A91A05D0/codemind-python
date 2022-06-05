n=int(input())
ls=list(map(int,input().split()))
c=0
d=0
l=[]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if i!=j:
            if ls[i]==ls[j]:
                c=1
    if c==0:
        d=1
        l.append(ls[i])
if d==0:
    print('-1')
else:
    print(*l)