x=input()
x=x.lower()
li=[]
for i in x:
    if i not in "aeiouy":
        li.append(i)
y=".".join(li)
print("."+y)