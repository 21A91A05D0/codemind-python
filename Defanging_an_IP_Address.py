s=input()
k=''
for i in s:
    if i=='.':
        k+=''.join('[.]')
    else:
        k+=''.join(i)
print(k)