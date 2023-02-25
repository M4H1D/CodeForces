n=int(input())
x=input()[:n]
x=x+" " #একটা এক্সট্রা স্ট্রিং এড করলাম
li=[]
for i in range(n):
    if x.count("R")==n or x.count("G")==n or x.count("B")==n:
        print(n-1)
        exit()
    elif x[i]==x[i+1]: #১ম অক্ষর যদি ২য় অক্ষরের সমান হলে
        li.append(1)
    else:
        li.append(0)
print(sum(li))

