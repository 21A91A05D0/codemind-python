s=input()
s=s.lower()
s=set(s)
c=0
for i in s:
    if i!=' ':
        c+=1
print(c)