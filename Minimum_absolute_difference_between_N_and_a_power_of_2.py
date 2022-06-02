from math import floor,log2
n=int(input())
l=2**floor(log2(n))
r=l*2
a=n-l
b=r-n
if a>=b:
    print(b)
else:
    print(a)