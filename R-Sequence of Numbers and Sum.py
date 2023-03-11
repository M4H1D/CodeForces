while True:
    n,m=map(int,input().split())
    total=0
    if n<=0 or m<=0:
        break
    else:
        x=min(n,m);y=max(n,m)
        for i in range(x,y+1):
            total+=i
            print(i,end=' ')
        print(f"sum ={total}",end='')
        print()