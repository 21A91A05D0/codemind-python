def spit(n):
    s=0
    while n>0:
        d=n%10
        s+=d
        n=n//10
    return s   

n=int(input())
n=spit(n)
while True:
    s=spit(n)
    if s<10:
        d=s
        break
    n=s
print(d)