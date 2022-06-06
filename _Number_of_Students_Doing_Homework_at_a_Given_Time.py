n=int(input())
ls=list(map(int,input().split()))
m=int(input())
lst=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,n):
    for j in range(ls[i],lst[i]+1):
        if j==k:
            c+=1
print(c)