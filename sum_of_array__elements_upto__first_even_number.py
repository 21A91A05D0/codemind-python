n=int(input())
ls=list(map(int,input().split()))
s=0
for i in range(0,n):
    if ls[i]%2==0:
        break
    s+=ls[i]
print(s)
        