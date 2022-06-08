n=int(input())
ls=list(map(int,input().split()))
k=int(input())
p=max(ls)
for i in range(0,n):
    if (ls[i]+k)>=p:
        print('True',end=' ')
    else:
        print('False',end=' ')