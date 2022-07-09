n=int(input())
ls=list(map(int,input().split()))
s,c=0,0
for i in ls:
    s+=i
d=(s//n)
for i in ls:
    if i<=d:
        c+=1
print(c)