s=input()
l=s.split()
k=[]
for i in l:
    k.append(len(i))
print(min(k))