s=input()
n='0123456789'
c=0
for i in s:
    if i in n:
        c+=int(i)
print(c)