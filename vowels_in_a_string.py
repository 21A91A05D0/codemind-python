s=input()
c=input()
d,k=0,0
for i in s:
    if i==c:
        k=1
        d=s.index(i)
if k==1:
    print('True')
    print(d)
else:
    print('False')