n,m=map(int,input().split())
c=0
if n<2:
    print('Player 2')
else:
    while True:
        k=n//2 
        c+=1 
        if k<2: 
            break 
        n=k 
    if c%2==0:
        print('Player 1') 
    else: 
        print('Player 2')