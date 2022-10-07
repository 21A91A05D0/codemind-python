r,c=map(int,input().split())
m=[]
s,t=0,0
for i in range(r):
    ls=list(map(int,input().split()))
    m.append(ls)
for i in range(r):
    for j in range(c):
        if m[i][j]%2==0:
            s+=m[i][j]
        if m[i][j]%2!=0:
            t+=m[i][j]
print(s,t)