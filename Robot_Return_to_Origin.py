s=input()
n='RU'
c=0
k='LD'
for i in s:
    if i in n:
        c+=1
    if i in k:
        c-=1
if c==0:
    print('True')
else:
    print('False')