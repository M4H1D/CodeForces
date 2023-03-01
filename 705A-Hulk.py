n=int(input())
x="I hate it"
for i in range(1,n+1):
    if n==1:
        print(x)
        exit()
    elif n>1 and i%2==0:
        x=x.replace("it","that I love it")
    elif n>1 and i%2!=0:
        x=x.replace("it","that I hate it")
print(x[12:])