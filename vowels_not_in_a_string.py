s=input().lower()
n='aeiou'
c=0
for i in n:
    if i not in s:
        print(i,end=' ')
    else:
        c+=1
if c==len(n):
    print('0')