n=int(input())
ls=list(map(int,input().split()))
l=[]
c,d=1,0
for i in range(0,n):
    if ls[i]>0:
        c=1
        for j in range(i+1,n):
            if ls[i]==ls[j]:
                c+=1
                ls[j]=-1
        if c==1:
            d=1
            l.append(ls[i])
if d==0:
    print('-1')
else:
    print(max(l))