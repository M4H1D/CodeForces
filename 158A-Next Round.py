n,x=map(int,input().split())
li=list(map(int,input().split()))[:n]
li2=[]
x-=1
for i in li:
    if sum(li)==0:
        print(0)
        exit()

    elif i>0 and i>=li[x]:
        li2.append(i)
print(len(li2))
