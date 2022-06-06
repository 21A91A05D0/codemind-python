t=int(input())
for i in range(0,t):
    s=input()
    c=0
    for i in range(0,len(s)):
        if s[i]>='1' and s[i]<='9':
            c=1
    if c==1:
        print('Yes')
    else:
        print('No')