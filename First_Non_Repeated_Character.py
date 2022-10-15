t=int(input())
while t:
    n=int(input())
    s=input()
    c=''
    for i in s:
        if s.count(i)==1:
            c=i
            break
    if len(c)==0:
        print(-1)
    else:
        print(c)
    t-=1