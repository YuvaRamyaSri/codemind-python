s=input()
v="aeoiuAEIOU"
b=[]
f=0
for i in s:
    if i in v and i not in b:
        b.append(i)
        f=1
        print(i,end=" ")
if(f==0):
    print(-1)