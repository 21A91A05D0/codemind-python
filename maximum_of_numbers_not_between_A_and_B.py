n=int(input())
ls=list(map(int,input().split()))
l,m=map(int,input().split())
lst=[]
d=0
for i in range(0,n):
    if ls[i]>l and ls[i]>m:
        lst.append(ls[i])
        d+=1
if d==0:
    print('-1')
else:
    print(max(lst))