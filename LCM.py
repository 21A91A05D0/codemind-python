n,m=map(int,input().split())
if n>=m:
    r=n
else:
    r=m
while(1):
    if (r%n==0) and (r%m==0):
        print(r,end='')
        break
    r+=1
    
