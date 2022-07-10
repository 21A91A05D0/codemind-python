n=int(input())
a=n*n
n=str(n)
a=str(a)  #144
b=a[::-1] #441
c=n[::-1] #21
d=int(c)
e=d*d  #441
f=str(e)
h=f[::-1]
if h==a:
    print('True')
else:
    print('False')