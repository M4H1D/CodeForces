from math import ceil as c
n,k=map(int,input().split())
odd=c(n/2)
if k<=odd:
    result=(k*2)-1
else:
    result=(k-odd)*2
print(result)