n=input().lower().replace("","")
n=n.split()
m=0
for i in n:
    v="aeiouAEIOU"
    c=0
    for j in i:
        if(j in v):
            c+=1
    if(m<c):
        m=c
print(m)