n=input()
c=0
for i in n:
    if n.count(i)>1:
        c=1
        break
if c==0:
    print('Unique Number')
else:
    print('Not Unique Number')
