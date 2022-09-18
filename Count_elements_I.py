n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=0
c=[]
for i in a:
    if(i in b and i not in c):
        c.append(i)
print(len(c))