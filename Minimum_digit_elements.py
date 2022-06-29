def rev(n):
    re=0
    while n>0:
        d=n%10
        re+=1
        n=n//10
    return re

n=int(input())
s=list(map(int,input().split()))
l=[]
for i in range(0,n):
    l.append(rev(s[i]))
print(l.count(min(l)))