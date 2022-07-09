n=int(input())
ls=list(map(int,input().split()))
k=int(input())
s=0
for i in range(0,n):
    s+=ls[i]
    if ls[i]%k==0:
        break
print(s)