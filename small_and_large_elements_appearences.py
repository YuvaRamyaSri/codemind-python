n=input()
m=19000
p=0
c=0
cou=0
for i in n:
    if(i!=" " and ord(i)<m):
        m=ord(i)
        p=i
q=max(n)
for i in n:
    if(i==p):
        c+=1
    elif(i==q):
        cou+=1
print(p,c,q,cou)