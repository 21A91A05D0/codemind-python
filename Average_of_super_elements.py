n=int(input())
ls=list(map(int,input().split()))
l=[]
c=0
for i in range(0,n):
    c=ls.count(ls[i])
    if ls[i]==c:
        l.append(ls[i])
if len(l)==0:
    print(-1)
else:
    p=set(l)
    s=0
    for i in p:
        s+=i
    avg=s/len(p)
    print("%.2f" %avg)