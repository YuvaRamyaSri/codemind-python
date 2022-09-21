n=input().lower().replace(" "," ")
m=input().lower().replace(" "," ")
c=0
p=[]
for i in n:
    for j in m:
        if(i==j and i!=" " and i not in p):
            p.append(i)
            c+=1
print(c)