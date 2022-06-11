a=list(map(int,input().split()))[:3]
b=list(map(int,input().split()))[:3]
k=0
j=0
for i in range(3):
    if(a[i]<b[i]):
        j+=1
    elif(a[i]>b[i]):
        k=k+1
print(k,j)