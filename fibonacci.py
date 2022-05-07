def fiba(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return (fiba(n-1)+fiba(n-2))
    
n=int(input())
for i in range(0,n):
    res=fiba(i)
    print(res,end=' ')