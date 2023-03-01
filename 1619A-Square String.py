for _ in range(int(input())):
    s=input()
    if len(s)%2==1:
        print("NO")
    else:
        x=int(len(s)/2)
        if s[0:x]==s[x:len(s)]:
            print("YES")
        else:
            print("NO")