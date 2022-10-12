l=list(input())
s='0123456789'
c=0
for i in l:
    if i in s:
        c+=int(i)
print(c)