n=input()
n=n.split()
p=0
q=0
for i in n:
    p=min(i)
    q=max(i)
    print(p,q,end=" ")