n=int(input())
c=0
for i in range(1,n+1):
    if i*(i+1)==n:
        c=1
        print('YES')
if c==0:
    print('NO')
