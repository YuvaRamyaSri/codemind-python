a=input().replace(' ','')
a=a.lower()
s=[]
for i in a:
    c=a.count(i)
    if(c==1 and i!=" "):
        s.append(i)
print("".join(sorted(s)))