n=int(input())
ls=list(map(int,input().split()))
s,c=0,0
for i in ls:
    if i%2==0:
        s+=i
    else:
        c+=i
if s>c:
    print(s-c)
else:
    print(c-s)
