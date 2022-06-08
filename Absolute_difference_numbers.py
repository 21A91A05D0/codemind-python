
def emo(n, k):
    f=0
    while k>0:
        d=n%10
        f=f*10+d
        n=n//10
        k-=1
    return f
def rever(n):
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev

n,k=map(int,input().split())
l=rever(n)
p=emo(n,k)
a=rever(p)
y=emo(l,k)
print(abs(a-y))
