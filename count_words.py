def fun(i):
    l=len(i)
    c=0
    if i[0] in 'AEIOUaeiou' and i[l-1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz':
        
        c+=1
    return c

s=input()
l=s.split()
p=0
for i in l:
    p+=fun(i)
print(p)