n=int(input())
m=0
for i in range(1,n+1):
    if(n%i==0):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c+=1
        if(c!=0):
            m+=1
print(m+1)