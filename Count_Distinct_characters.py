n=input().lower()
c=[]
for i in n:
    if(i not in c and i!=" "):
        c.append(i)
c.sort()
print(len(c))