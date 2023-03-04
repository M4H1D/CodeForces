for _ in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if (a<b and c<d and a<c and b<d):
        print("Yes")
    else:
        e=a
        a=b
        b=d
        d=c
        c=e
        if(a<b and c<d and a<c and b<d):
            print("Yes")
        else:
            e=a
            a=b
            b=d
            d=c
            c=e
            if(a<b and c<d and a<c and b<d):
                print("Yes")
            else:
                e=a
                a=b
                b=d
                d=c
                c=e
                if(a<b and c<d and a<c and b<d):
                    print("Yes")
                else:
                    print("No")