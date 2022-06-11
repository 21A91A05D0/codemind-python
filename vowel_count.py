s=input()
d,k=0,0
for i in s:
    if i in 'AEIOUaeiou':
        k=1
        d+=1
if k==0:
    print('0')
else:
    print(d)
