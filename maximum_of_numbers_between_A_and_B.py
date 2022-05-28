n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())
l=[ ]
f=0
for i in range(0,n):
    if ls[i]>=a and ls[i]<=b:
        f+=1
        l.append(ls[i])
        
if f==0:
    print('-1')
m=l[0]
for j in range(len(l)):
    if m<l[j]:
        m=l[j]
print(m)

    