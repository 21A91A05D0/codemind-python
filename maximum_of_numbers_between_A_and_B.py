n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
c=0
for i in ls:
    if i>=a and i<=b:
        c=1
        l.append(i)
if c==0:
    print('-1')
else:
    print(max(l))