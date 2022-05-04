a,b,c=map(float,input().split())
s=(a+b+c)/2
k=(s*(s-a)*(s-b)*(s-c))
p=k**0.5
print("%.2lf" %p)