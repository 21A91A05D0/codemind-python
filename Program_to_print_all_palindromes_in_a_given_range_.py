a=int(input())
b=int(input())
for i in range(a,b+1):
    rev=0
    t=i
    while i>0:
        d=i%10
        rev=rev*10+d
        i=i//10
    if rev==t:
        print(t,end=' ')