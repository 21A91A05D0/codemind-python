n,m=map(int,input().split())
ls=list(map(int,input().split()))
c=0
for i in range(len(ls)):
    if ls[i]%m==0:
        c+=1
print(c)