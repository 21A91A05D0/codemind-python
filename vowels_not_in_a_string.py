s=input().lower()
n='aeiou'
l=[]
for i in s:
    if i in n:
        l.append(i)
if len(set(l))==len(n):
    print(0)
else:
    for i in n:
        if i not in l:
            print(i,end=" ")