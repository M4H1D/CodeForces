for _ in range(int(input())):
    a,b=map(str,input().split())
    if (a.count("S")==1 or a.count("M")==1 or a.count("L")==1) and (b.count("S")==1 or b.count("M")==1 or b.count("L")==1):
        if a[-1]=="S" and b[-1]=="M":
            print("<")
        elif a[-1]=="S" and b[-1]=="L":
            print("<")
        elif a[-1]=="M" and b[-1]=="S":
            print(">")
        elif a[-1]=="M" and b[-1]=="L":
            print("<")
        elif a[-1]=="L" and b[-1]=="S":
            print(">")
        elif a[-1]=="L" and b[-1]=="M":
            print(">")
        elif a[-1]=="S" and b[-1]=="S":
            if len(a)>len(b):
                print("<")
            elif len(a)==len(b):
                print("=")
            else:
                print(">")
        elif a[-1]=="M" and b[-1]=="M":
            if len(a)>len(b):
                print(">")
            elif len(a)==len(b):
                print("=")
            else:
                print("<")
        elif a[-1]=="L" and b[-1]=="L":
            if len(a)>len(b):
                print(">")
            elif len(a)==len(b):
                print("=")
            else:
                print("<")
