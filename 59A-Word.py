s=str(input())
if sum(map(str.isupper,s))>sum(map(str.islower,s)):
    print(s.upper())
else:
    print(s.lower())