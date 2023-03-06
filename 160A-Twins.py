n=int(input())
li=list(map(int,input().split()))[:n]
li.sort()
li.reverse()
total=sum(li)
coin=0
money=0
if(n==1 or (n==2 and total%2==0)):
    print(n)
    exit()
elif (n>=2):
    for i in li:
        money+=i
        coin+=1
        if money>(total//2) :
            break
print(coin)


