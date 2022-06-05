t=int(input())
for i in range(0,t):
    l=''
    s=input()
    l = "".join(reversed(s))
    if l==s and len(s)%2==0:
        print('YES EVEN')
    elif l==s and len(s)%2!=0:
        print('YES ODD')
    else:
        print('NO')