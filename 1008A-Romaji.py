#######<786>#######
#######[_PUTIN Still Alive_]######
######Let's rock and Roolllll#####
'''
Loading Putin_er_KHel...99%################
'''



s = input()
v=['a','e','i','o','u']
total=len(s)
for i in range(total):
    if s[i] in v or s[i]=='n':
        continue
    else:
        if i==total-1:
            print('NO')
            exit(0)
        else:
            if s[i+1] not in v:
                print('NO')
                exit(0)
print('YES')