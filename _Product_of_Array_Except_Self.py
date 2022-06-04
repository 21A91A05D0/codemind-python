n=int(input())
ls=list(map(int,input().split()))
p=1
for i in range(0,n):
    p=1
    for j in range(0,n):
        if ls[i]!=ls[j]:
            p*=ls[j]
    print(p,end=' ')