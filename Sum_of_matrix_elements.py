r=int(input())
c=int(input())
m=[]
s=0
for i in range(r):
    ls=list(map(int,input().split()))
    m.append(ls)

for i in range(r):
    for j in range(c):
        s+=m[i][j]
print(s)
