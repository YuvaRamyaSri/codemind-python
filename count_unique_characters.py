n=input().lower()
c=[]
for i in n:
    if(n.count(i)==1 and i!=" "):
        c.append(i)
c.sort()
print(len(c))