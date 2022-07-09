n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls[::-1]:
    if i%2==0:
        print(i)
        break