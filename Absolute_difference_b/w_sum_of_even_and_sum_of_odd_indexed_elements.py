#import math
n=int(input())
ls=list(map(int,input().split()))
s,s1=0,0
for i in range(0,n):
    if i%2==0:
        s+=ls[i]
    if i%2!=0:
        s1+=ls[i]
print(abs(s1-s))

