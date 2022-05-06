n=int(input())
sq=n**2  #144
rev=0
while(n):
    d=n%10
    rev=rev*10+d  #21
    n=n//10
sqr=rev**2   #441
rev1=0
while(sqr):
    d=sqr%10
    rev1=rev1*10+d  #144
    sqr=sqr//10
if sq==rev1:
    print('True')
else:
    print('False')
