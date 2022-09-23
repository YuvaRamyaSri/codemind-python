n=input()
n=n.lower()
p=[]
c=0
for i in n:
    if(i not in p):
        p.append(i)
        c+=1
if(c==len(n)):
    print("True")
else:
    print("False")