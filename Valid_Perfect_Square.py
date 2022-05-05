t=int(input())
for j in range(0,t+1):
    n=int(input())
    c=0
    for i in range(1,n):
        if i*i==n:
            c=1
            print('True')
            break
    if c==0:
        print('False')