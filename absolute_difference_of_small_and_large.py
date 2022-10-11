s=input().split()
l=[]
for i in s:
    a=ord(min(i))
    b=ord(max(i))
    l.append(int(b)-int(a))
print(*l)