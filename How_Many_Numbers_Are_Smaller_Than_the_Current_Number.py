n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(l[i]>l[j] and i!=j):
            c+=1
    print(c,end=" ")