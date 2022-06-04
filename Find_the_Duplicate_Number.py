n=int(input())
ls=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if ls[i]==ls[j]:
            p=ls[j]
print(p)