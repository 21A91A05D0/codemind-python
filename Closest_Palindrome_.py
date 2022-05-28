def fun(n):
    t=n
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==t:
        return 1
    return 0

n=int(input())
t=n
i=1
while True:
    if fun(n+i)==1:
        k=(n+i)
        break
    i+=1
for j in range(n-1,0,-1):
    if fun(j)==1:
        l=j
        break
if abs(k-n)==abs(l-n):
    print(l,k)
elif abs(k-n)>abs(l-n):
    print(l)