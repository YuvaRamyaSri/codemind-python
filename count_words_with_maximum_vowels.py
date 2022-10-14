n=input().split()
v="aeiouAEIOU"
dup=[]
for i in n:
    c=0
    p=[]
    for j in i:
        if(j in v and j not in p):
            c+=1
    dup.append(c)
r=0
for i in dup:
    if(i==min(dup)):
        r+=1
print(r)