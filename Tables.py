n,m=map(int,input().split())
p=1
for i in range(1,m+1):
    if i%2!=0:
        p=n*i
        print(n,"x",i,"=",p)