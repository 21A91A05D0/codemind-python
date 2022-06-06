s=input()
d=s[0]
for i in range(0,len(s)):
    if d<s[i]:
        d=s[i]
print(d)