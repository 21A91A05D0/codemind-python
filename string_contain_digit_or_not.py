s=input()
c,d=0,0
for i in range(0,len(s)):
    if s[i]>='0' and s[i]<='9':
        c=1
        d+=1
if c==1:
    print('Contains ' "%.0f" ' digit' %d)
else:
        print("Doesn't contain digit")