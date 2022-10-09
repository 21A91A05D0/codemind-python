s=input()
s=s.lower()
f=set(s)
l=f
c=''
k=''
for i in l:
    if i!=' ':
        c+=i
c=''.join(sorted(c))
print(c)