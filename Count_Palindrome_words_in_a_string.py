s=input()
s=s.lower()
s=s.split()
c=0
for i in s:
    if i[::-1]==i:
        c+=1
print(c)