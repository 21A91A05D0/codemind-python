def square(n):
    for i in range(1,n+1):
        c=0
        if i*i==n:
            c+=1
            break
    if c==1:
        return 1
    else:
        return 0

n=int(input())
ls=list(map(int,input().split()))
s=0
for i in range(0,n):
    p=square(ls[i])
    if p==1:
        s+=ls[i]
print(s)