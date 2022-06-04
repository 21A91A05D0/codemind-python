t=int(input())
for j in range(1,t+1):
    n=int(input())
    ls=list(map(int,input().split()))
    l=[]
    i=n//2
    while i>0:
        a=max(ls)
        l.append(a)
        ls.remove(a)
        b=min(ls)
        l.append(b)
        ls.remove(b)
        i-=1
    if n%2!=0:
        l.append(ls[i])
    print(*l)
