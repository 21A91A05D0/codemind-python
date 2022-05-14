def fiba(n):
    a,b=0,1
    while True:
        c=a+b
        a=b
        b=c       #same code print b---after fiba
        if c>n:
            if (a-n)>(n-b):
                print(a)
            elif (a-n)==(n-b):
                print(a,b)
            else:
                print(b)
            break

n=int(input())
fiba(n)