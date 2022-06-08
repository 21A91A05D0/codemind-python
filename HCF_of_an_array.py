n=int(input())
ls=list(map(int,input().split()))
p=ls[0]
j=1
while j<n:
    if ls[j]%p==0:
        j+=1
    else:
        p=ls[j]%p
print(p)
        