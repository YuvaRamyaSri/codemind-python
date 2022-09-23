n=input()
n=n.lower()
p=[]
c=0
n=n.split()
n=n[::-1]
for i in range(len(n)):
    n[i]=n[i][::-1]
    print(n[i],end=" ")