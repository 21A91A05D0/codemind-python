s=input()
ch=input()
l=len(s)
c=0
for i in range(0,l):
    if s[i]==ch:
        c+=1
if c==0:
    print('-1')
else:
    print(c)