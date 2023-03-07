n,k=map(int,input().split())
baki=240-k
korbe=0
koita=0
if (1<=n<=10 and 1<=k<=240):
    for i in range(1,n+1):
        korbe+=(5*i)
        if baki>=korbe:
            koita+=1
print(koita)
