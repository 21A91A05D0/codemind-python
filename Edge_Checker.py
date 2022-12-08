a,b=map(int,input().split())
if (a+b)==11:
    print('Yes')
elif abs(b-a)==1:
    print('Yes')
else:
    print('No')