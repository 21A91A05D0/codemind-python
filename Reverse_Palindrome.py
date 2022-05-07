def reverse(n):
    rev=0
    while(n):
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev    

n=int(input())
r=reverse(n)
n+=r
while(True):
    r=reverse(n)
    if r==n:
        print(n)
        break
    n+=r