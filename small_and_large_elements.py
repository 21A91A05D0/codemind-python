s=input()
l=s.split()
p=0
for i in l:
    print(min(i),end=' ')
    break
for i in l[::-1]:
    print(max(i),end=' ')
    break