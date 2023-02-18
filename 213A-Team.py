#213A-Team
li=[]
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x+y+z>1:
        li.append(1)
print(sum(li))
li=[]
