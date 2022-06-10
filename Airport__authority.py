n=int(input())
ls=[]
for i in range(0,n):
    l=int(input())
    ls.append(l)
k=int(input())
c=0
for i in ls:
    if i<=k:
        c+=1
    else:
        c+=2
print(c)

    