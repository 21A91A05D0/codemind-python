n=int(input())
ls=list(map(int,input().split()))
l=[]
c=0
for i in range(0,n):
    c=ls.count(ls[i])
    if ls[i]==c:
        l.append(ls[i])
l=set(l)
k=l
print(len(k))