n=input().lower().replace("","")
n=n.split()
for i in n:
    v="aeiouAEIOU"
    c=0
    for j in i:
        if(j in v):
            c+=1
    print(c,end=" ")