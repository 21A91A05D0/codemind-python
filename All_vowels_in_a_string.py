s=input()
n='aeiou'
c=0
for i in n:
    if i in s:
        c+=1
if c==len(n):
    print('True')
else:
    print('False')
        