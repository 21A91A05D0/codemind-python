s=input()
g=input()
c=0
for i in range(len(s)):
    if s[i]==g:
        c=1
        d=i
        break
if c==1:
    print('True')
    print(d)
else:
    print('False')
