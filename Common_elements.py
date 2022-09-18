n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
p=0
for i in a:
    if(i in b and i not in c):
        c.append(i)
        p+=1
for i in c:
    print(i,end=" ")