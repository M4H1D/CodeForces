num=int(input())
s=input()
s1=s.upper()
s1=s1[:num]
if s1.count("A")>s1.count("D"):
    print("Anton")
elif s1.count("A")==s1.count("D"):
    print("Friendship")
else:
    print("Danik")