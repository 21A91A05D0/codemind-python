n=int(input())
l=list(map(int,input().split()))
c,j=0,0
for i in range(0,n):
    for j in range(i,n):
        if l[i]<l[j]:
            c=1
if c==1:
    print('no')
else:
    print('yes')