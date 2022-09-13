n=int(input())
p=[]
while(n!=0):
    d=n%10
    n=n//10
    p.append(d)
c=[]
for i in p:
    if(i not in c):
        c.append(i)
if(len(p)==len(c)):
    print("Unique Number")
else:
    print("Not Unique Number")