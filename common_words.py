n=input().lower().replace(" "," ")
m=input().lower().replace(" "," ")
n=n.split()
m=m.split()
for i in m:
    if(i!=" " and i in n):
        print(i,end=" ")