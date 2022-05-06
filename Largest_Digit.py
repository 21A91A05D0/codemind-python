n=int(input())
rev=0
c=0
while(n):
    d=n%10
    if d>c:
        c=d
    n=n//10
print(c)