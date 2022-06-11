def fun(i):
    return i[0]

s=input()
l=s.split()
p=0
for i in l[::-1]:
    p=fun(i)
    break
print(p)