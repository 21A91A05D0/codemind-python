def rev(n):
    re=0
    while n>0:
        d=n%10
        re+=d
        n=n//10
    return re

n=int(input())
s=list(map(int,input().split()))
s1=0
l=[]
for i in range(0,n):
    r=rev(s[i])
    s1+=r
print(s1)