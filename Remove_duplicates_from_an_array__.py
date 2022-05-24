n=int(input())
ls=list(map(int,input().split()))
#print(*ls)
for i in range(0,n):
    for j in range(i+1,n):
        if ls[i]==ls[j]:
            ls[j]=-1
for i in range(0,n):
    if ls[i]>-1:
        print(ls[i],end=' ')
        