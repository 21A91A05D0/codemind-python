def fun(i):
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    return c

s=input()
l=s.split()
p=[]
for i in l:
    p.append(fun(i))
print(min(p))