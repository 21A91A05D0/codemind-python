def rev(n):
    re=0
    t=n
    while n>0:
        d=n%10
        re=re*10+d
        n=n//10
    if re==t:
        return 1

n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(0,n):
    if rev(s[i])==1:
        c+=1
print(c)