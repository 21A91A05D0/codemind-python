n=int(input())
ls=list(map(int,input().split()))
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if ls[i]==ls[j]:
                ls[j]=-1
for j in ls:
    if j>-1:
        print(j,end=' ')