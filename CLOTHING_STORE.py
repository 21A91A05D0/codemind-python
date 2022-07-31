n=int(input())
ls=list(map(int,input().split()))
k=[]
o=0
l=set(ls)
p=l
for i in p:
    k.append(ls.count(i))
for i in k:
    o+=(i//2)
print(o)
