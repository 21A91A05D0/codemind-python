def rev(n):
    re=0
    while n>0:
        d=n%10
        re=re*10+d
        n=n//10
    return re

n=int(input())
s=list(map(int,input().split()))
for i in range(0,n):
    print(rev(s[i]),end=' ')