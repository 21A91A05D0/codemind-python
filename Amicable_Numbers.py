n=int(input())
m=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if m==s:
    print('Amicable')
else:
    print('Not Amicable')