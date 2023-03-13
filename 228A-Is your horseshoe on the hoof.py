
li=list(map(int,input().split()))[:4];count=0;n=0
if len(li)>len(set(li)):
    count=(len(li)-len(set(li)))

print(count)