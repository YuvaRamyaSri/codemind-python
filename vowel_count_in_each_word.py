l=list(map(str,input().split()))
d=[]
for i in l:
    count=0
    for j in i:
        if j in "AEIOUaeiou":
            count=count+1
    d.append(count)
for i in d:
    print(i,end=" ")