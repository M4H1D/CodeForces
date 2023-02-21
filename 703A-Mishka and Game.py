li_m=[]
li_c=[]
for i in range(int(input())):
    m,c=map(int,input().split())
    if m>c:
        li_m.append(1)
    elif m<c:
        li_c.append(1)
    else:
        li_c.append(0)
        li_m.append(0)
if sum(li_m)>sum(li_c):
    print("Mishka")
elif sum(li_m)<sum(li_c):
    print("Chris")
else:
    print("Friendship is magic!^^")
