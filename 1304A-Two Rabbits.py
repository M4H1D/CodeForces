for _ in range(int(input())):
    x,y,a,b=map(int,input().split())
    z=a+b
    if(y-x) % z!=1:
        print((y-x)//z)
    else:
        print("-1")