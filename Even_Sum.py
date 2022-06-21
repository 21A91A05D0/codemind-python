
n=int(input())
ls=list(map(int,input().split()))
s,s1=0,0
for i in range(0,n):
    if ls[i]%2==0:
        s+=ls[i]
print(s)
