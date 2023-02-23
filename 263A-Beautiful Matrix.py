a=list(map(int,input().split()))[:5]
b=list(map(int,input().split()))[:5]
c=list(map(int,input().split()))[:5]
d=list(map(int,input().split()))[:5]
e=list(map(int,input().split()))[:5]
if sum(a)!=0:
    row=1
    col=a.index(1)+1
elif sum(b)!=0:
    row=2
    col=b.index(1)+1
elif sum(c)!=0:
    row=3
    col=c.index(1)+1
elif sum(c)!=0:
    row=4
    col=c.index(1)+1
else:
    row=5
    col=c.index(1)+1
print(abs(row-3)+abs(col-3))
