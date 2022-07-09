n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in ls:
    if i<a or i>b:
        s+=i
print(s)