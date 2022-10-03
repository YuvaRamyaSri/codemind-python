n=input()
n=n.split()
p=0
q=0
for i in n:
    p=min(i)
    break
n=n[::-1]
for i in n:
    q=max(i)
    break
print(p,q)