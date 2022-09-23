n=input()
n=n.lower()
p=0
c=0
n=n.split()
for i in n:
    p=len(i)
    if(c<p):
        c=p
print(c)