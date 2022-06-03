n=int(input())
ls=[ ]
while n>0:
    d=n%10
    ls.append(d)
    n=n//10
j=1
c,i=0,0
for i in ls:
    for j in ls:
        if i==j:
            c+=1
if c==len(ls):
    print('Unique Number')
else:
    print('Not Unique Number')