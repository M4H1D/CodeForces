for _ in range(int(input())):
    x,y=map(int,input().split())
    x=abs(x);y=abs(y)
    if x==y:
        print(abs(x+y))
    else:
        z=max(abs(x),abs(y))
        print(2*abs(z)-1)