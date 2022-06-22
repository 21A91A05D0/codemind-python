n=int(input())
m=int(input())
for i in range(n,m+1):
    c=0
    r=0
    t=i
    while(t):
        d=t%10
        if d!=0 and i%d==0:
            c+=1
        r+=1    
        t=t//10
    if c==r:
        print(i,end=' ')
