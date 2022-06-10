def fact(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s

ls=list(map(int,input().split(',')))
l=[]
c=0
for i in ls:
    p=fact(i)
    if p in ls:
        c=1
        l.append(i)
if c==0:
    print('-1')
else:
    print(*sorted(l))

    