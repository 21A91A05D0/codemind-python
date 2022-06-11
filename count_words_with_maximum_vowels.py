def fun(i):
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    return c

s=input()
l=s.split()
k=[]
for i in l:
    p=fun(i)
    k.append(p)
print(k.count(max(k)))