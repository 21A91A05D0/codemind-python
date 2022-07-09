n=int(input())
ls=list(map(int,input().split()))
k=int(input())
l=[]
c=0
for i in range(0,n):
    if ls.count(ls[i])==k:
        c=1
        l.append(ls[i])
if c==0:
    print('-1')
else:
    print(*set(l))