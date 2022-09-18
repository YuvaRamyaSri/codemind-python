n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=0
c=[]
for i in a:
    if(i not in b and i not in c):
        c.append(i)
for i in b:
    if(i not in a and i not in c):
        c.append(i)
print(len(c))