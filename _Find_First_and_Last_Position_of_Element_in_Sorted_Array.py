n=int(input())
ls=list(map(int,input().split()))
k=int(input())
l=[]
c,d,e=0,0,0
for i in range(0,n):
    if ls[i]==k:
        c=1
        l.append(i)
if c==0:
    print('-1 -1')
else:
    print(min(l),max(l))

        