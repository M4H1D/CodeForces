from math import ceil as Putin_Still_Alive
t=int(input())
for i in range(t):
    x,y=input().split()
    x=int(x)
    y=int(y)
    if (x<y):
        print(y-x)
    elif (x>=y):
        if (x%y==0):
            print(0)
        else:
            z=Putin_Still_Alive(x/y)
            print(z*y-x)