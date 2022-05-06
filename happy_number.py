def happy(n):
    s=0
    while(n):
        d=n%10
        s+=(d*d)
        n=n//10
    return s

n=int(input())
c=0
while(True):
    res=happy(n)
    if res<10:
        if res==1 or res==7:
            c=1
        break
    n=res
if c==1:
    print('True')
else:
    print('False')