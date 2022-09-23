n=input().lower().replace("","")
n=n.split()
p=[]
for i in n:
    v="aeiouAEIOU"
    c=0
    m=0
    for j in i:
        if(j in v):
            c+=1
    p.append(c)
print(min(p))