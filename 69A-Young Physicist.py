li1=[]
li2=[]
li3=[]
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    li1.append(x)
    li2.append(y)
    li3.append(z)
if sum(li1)==sum(li2)==sum(li3)==0:
    print("YES")
else:
    print("NO")
