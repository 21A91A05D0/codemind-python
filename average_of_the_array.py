n=int(input())
ls=list(map(int,input().split()))
s=0
for i in range(len(ls)):
    s+=ls[i]
print('%.2f' %(s/n))