l=list(map(str,input().split()))
a,b=0,0
for i in range(len(l)):
    a+=ord(min(l[i]))
    b+=ord(max(l[i]))
print(abs(a-b))