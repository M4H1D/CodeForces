x,n=map(int,input().split())
for i in range(n):
    if x%10==0:
        x=x//10
    else:
        x-=1
print(x)