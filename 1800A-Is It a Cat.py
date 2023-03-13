for _ in range(int(input())):
    n=int(input())
    s=input().lower()[:n]
    x=''
    x+=s[0]
    for i in range(1,n):
        if s[i]!=s[i-1]:
            x+=s[i]
    if x=="meow":
        print("YES")
    else:
        print("NO")