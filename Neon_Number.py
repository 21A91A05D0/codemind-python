n=int(input())
r=n**2
s=0
while(r>0):
    d=r%10
    s=s+d
    r=r//10
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')