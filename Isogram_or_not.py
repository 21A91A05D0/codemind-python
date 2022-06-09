s=input()
c=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            c=1
if c==0:
    print('True')
else:
    print('False')