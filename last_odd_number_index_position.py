n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(len(ls)):
    if ls[i]%2!=0:
        c=i
print(c)