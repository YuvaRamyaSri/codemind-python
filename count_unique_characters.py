n=input().lower().replace(" "," ")
c=0
p=[]
for i in n:
    c=n.count(i)
    if(c==1 and i!=" "):
        p.append(i)
print(len(p))