n=int(input())
l=list(map(int,input().split()))
ls=[]
d=sum(l)
for i in l:
    if d%i==0:
        ls.append(i)
print(max(ls))