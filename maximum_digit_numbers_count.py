n=int(input())
ls=list(map(str,input().split()))
l,k=[],[]
for i in ls:
    l.append(len(i))
for i in ls:
    if len(i)==max(l):
        k.append(i)
print(*k)
        
