s=input()
s1=[]
for i in s:
    if i=="7":
        s1.append(i)
    elif i=="4":
        s1.append(i)
if len(s1)==7 or len(s1)==4:
    print("YES")
else:
    print("NO")
