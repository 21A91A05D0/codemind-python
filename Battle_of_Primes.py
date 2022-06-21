def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
m=int(input())
s=(n+m)
c=0
for i in range(s+1,100000):
    if isprime(i)==1:
        c=i
        break
print(c-s)