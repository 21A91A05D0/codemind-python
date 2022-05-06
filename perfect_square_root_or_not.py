n=int(input())
c=0
for i in range(1,n+1):
    if i*i==n:
        c=1
        print('True')
if c==0:
    print('False')