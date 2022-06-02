t=int(input())
for j in range(1,t+1):
    n,m=map(int,input().split())
    i=1
    k=0
    l=0
    for i in range(1,m+1):
        if (i*i)%m==n:
            l=i
            k=1
            break
    if k==0:
        print(-1)
    elif n==0:
        print('0')
    else:
        print(l)
    