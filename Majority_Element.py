n=int(input())
ls=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(i+1,n):
        if ls[i]==ls[j]:
            c+=1
    if(c>=int(n//2)):
        print(ls[i])