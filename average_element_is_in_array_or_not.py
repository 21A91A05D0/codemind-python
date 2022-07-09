n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    s+=i
if (s//n) in ls:
    print('True')
else:
    print('False')