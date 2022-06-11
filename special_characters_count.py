s=input()
s1=0
for i in s:
    if i.isalpha():
        continue
    elif i.isdigit():
        continue
    elif i==' ':
        continue
    else:
        s1+=1
print(s1)