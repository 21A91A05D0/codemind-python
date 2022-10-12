s=list(input())
k=0
for i in s:
    if s.count(i)==1:
        c=s.index(i)
        k=1
        break
if k==0:
    print(-1)
else:
    print(c)