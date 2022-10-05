x=list(map(str,input().split()))
e=0
o=0
for i in x:
    p=min(i)
    q=max(i)
    e+=ord(p)
    o+=ord(q)
print(abs(o-e))