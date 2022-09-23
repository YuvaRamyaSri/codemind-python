n=input()
n=n.lower()
p=[]
c=0
n=n.split()
for i in range(len(n)):
    if(i%2==0):
        n[i]=n[i][::-1]
        print(n[i],end=" ")
    else:
        print(n[i],end=" ")