s=input()
l=s.split()
for i in l:
    if l.index(i)%2==0:
        print(i[::-1],end=' ')
    else:
        print(i,end=' ')