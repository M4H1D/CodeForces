n=int(input())
s=input().lower()[:n]
li=list(s)
x=["a","e","i","o","u","y"]
for i in range(n-1,0,-1):
    if li[i-1] in x and li[i] in x:li.pop(i)
print("".join(li))