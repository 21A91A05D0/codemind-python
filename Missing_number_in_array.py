t=int(input())
while t:
    k=[]
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(1,n+1):
        k.append(i)
    for i in range(len(k)+1):
        if i in k and i not in l:
            print(i)
            break
    t-=1