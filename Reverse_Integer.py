n=int(input())
rev=0
f=0
if n<0:
    f=1
    n=abs(n)
while(n):
    d=n%10
    rev=rev*10+d
    n=n//10
if f==0:
    print(rev)
else:
    print("-%d" %rev)