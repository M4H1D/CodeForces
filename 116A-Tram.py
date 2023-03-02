li=[]
z=0
for _ in range(int(input())):
    x,y=map(int,input().split())
    z=z-x+y
    a=z
    li.append(a)
print(max(li))